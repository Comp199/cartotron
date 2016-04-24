BEGIN;
--
-- Create model Cart
--
CREATE TABLE "shop_cart" ("id" serial NOT NULL PRIMARY KEY, "session_id" varchar(50) NOT NULL, "created_date" timestamp with time zone NOT NULL);
--
-- Create model CartItem
--
CREATE TABLE "shop_cartitem" ("id" serial NOT NULL PRIMARY KEY, "quantity" integer NOT NULL CHECK ("quantity" >= 0), "cart_id" integer NOT NULL);
--
-- Create model Category
--
CREATE TABLE "shop_category" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(25) NOT NULL);
--
-- Create model Invoice
--
CREATE TABLE "shop_invoice" ("id" serial NOT NULL PRIMARY KEY, "created_date" timestamp with time zone NOT NULL, "stripe_token" varchar(100) NOT NULL, "city" varchar(30) NOT NULL, "country" varchar(20) NOT NULL, "postal_code" varchar(10) NOT NULL, "street_1" varchar(50) NOT NULL, "street_2" varchar(50) NOT NULL, "name_first" varchar(30) NOT NULL, "name_last" varchar(30) NOT NULL, "phone" varchar(15) NOT NULL, "total" numeric(10, 2) NULL, "shipping" numeric(10, 2) NOT NULL);
--
-- Create model LineItem
--
CREATE TABLE "shop_lineitem" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "description" varchar(50) NOT NULL, "price" numeric(10, 2) NOT NULL, "sku" varchar(50) NOT NULL, "quantity" integer NOT NULL CHECK ("quantity" >= 0), "invoice_id" integer NOT NULL);
--
-- Create model Product
--
CREATE TABLE "shop_product" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(50) NOT NULL, "price" numeric(10, 2) NOT NULL, "quantity" integer NOT NULL CHECK ("quantity" >= 0), "description" text NOT NULL, "sku" varchar(10) NOT NULL, "image" varchar(100) NOT NULL);
CREATE TABLE "shop_product_categories" ("id" serial NOT NULL PRIMARY KEY, "product_id" integer NOT NULL, "category_id" integer NOT NULL);
--
-- Add field product to lineitem
--
ALTER TABLE "shop_lineitem" ADD COLUMN "product_id" integer NULL;
ALTER TABLE "shop_lineitem" ALTER COLUMN "product_id" DROP DEFAULT;
--
-- Add field product to cartitem
--
ALTER TABLE "shop_cartitem" ADD COLUMN "product_id" integer NOT NULL;
ALTER TABLE "shop_cartitem" ALTER COLUMN "product_id" DROP DEFAULT;
ALTER TABLE "shop_cartitem" ADD CONSTRAINT "shop_cartitem_cart_id_6bf1447e_fk_shop_cart_id" FOREIGN KEY ("cart_id") REFERENCES "shop_cart" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "shop_cartitem_c44d83f7" ON "shop_cartitem" ("cart_id");
ALTER TABLE "shop_lineitem" ADD CONSTRAINT "shop_lineitem_invoice_id_240251f8_fk_shop_invoice_id" FOREIGN KEY ("invoice_id") REFERENCES "shop_invoice" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "shop_lineitem_f1f5d967" ON "shop_lineitem" ("invoice_id");
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categories_product_id_59c38762_fk_shop_product_id" FOREIGN KEY ("product_id") REFERENCES "shop_product" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categorie_category_id_7b004fe8_fk_shop_category_id" FOREIGN KEY ("category_id") REFERENCES "shop_category" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categories_product_id_edca6f84_uniq" UNIQUE ("product_id", "category_id");
CREATE INDEX "shop_product_categories_9bea82de" ON "shop_product_categories" ("product_id");
CREATE INDEX "shop_product_categories_b583a629" ON "shop_product_categories" ("category_id");
CREATE INDEX "shop_lineitem_9bea82de" ON "shop_lineitem" ("product_id");
ALTER TABLE "shop_lineitem" ADD CONSTRAINT "shop_lineitem_product_id_3ad21503_fk_shop_product_id" FOREIGN KEY ("product_id") REFERENCES "shop_product" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "shop_cartitem_9bea82de" ON "shop_cartitem" ("product_id");
ALTER TABLE "shop_cartitem" ADD CONSTRAINT "shop_cartitem_product_id_09e4b7dd_fk_shop_product_id" FOREIGN KEY ("product_id") REFERENCES "shop_product" ("id") DEFERRABLE INITIALLY DEFERRED;

COMMIT;
