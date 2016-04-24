BEGIN;
--
-- Create model Cart
--
CREATE TABLE "shop_cart" (
  "id"           SERIAL                   NOT NULL PRIMARY KEY,
  "session_id"   VARCHAR(50)              NOT NULL,
  "created_date" TIMESTAMP WITH TIME ZONE NOT NULL
);
--
-- Create model CartItem
--
CREATE TABLE "shop_cartitem" (
  "id"       SERIAL  NOT NULL PRIMARY KEY,
  "quantity" INTEGER NOT NULL CHECK ("quantity" >= 0),
  "cart_id"  INTEGER NOT NULL
);
--
-- Create model Category
--
CREATE TABLE "shop_category" (
  "id"   SERIAL      NOT NULL PRIMARY KEY,
  "name" VARCHAR(25) NOT NULL
);
--
-- Create model Invoice
--
CREATE TABLE "shop_invoice" (
  "id"           SERIAL                   NOT NULL PRIMARY KEY,
  "created_date" TIMESTAMP WITH TIME ZONE NOT NULL,
  "stripe_token" VARCHAR(100)             NOT NULL,
  "city"         VARCHAR(30)              NOT NULL,
  "postal_code"  VARCHAR(10)              NOT NULL,
  "street_1"     VARCHAR(50)              NOT NULL,
  "street_2"     VARCHAR(50)              NOT NULL,
  "name_first"   VARCHAR(15)              NOT NULL,
  "name_last"    VARCHAR(15)              NOT NULL,
  "country"      VARCHAR(20)              NOT NULL,
  "phone"        VARCHAR(15)              NOT NULL,
  "total"        NUMERIC(10, 2)           NULL,
  "shipping"     NUMERIC(10, 2)           NOT NULL
);
--
-- Create model LineItem
--
CREATE TABLE "shop_lineitem" (
  "id"          SERIAL         NOT NULL PRIMARY KEY,
  "name"        VARCHAR(50)    NOT NULL,
  "description" VARCHAR(50)    NOT NULL,
  "price"       NUMERIC(10, 2) NOT NULL,
  "sku"         VARCHAR(50)    NOT NULL,
  "product"     VARCHAR(50)    NOT NULL,
  "quantity"    INTEGER        NOT NULL CHECK ("quantity" >= 0)
);
--
-- Create model Product
--
CREATE TABLE "shop_product" (
  "id"          SERIAL         NOT NULL PRIMARY KEY,
  "name"        VARCHAR(50)    NOT NULL,
  "price"       NUMERIC(10, 2) NOT NULL,
  "quantity"    INTEGER        NOT NULL CHECK ("quantity" >= 0),
  "description" TEXT           NOT NULL,
  "sku"         VARCHAR(10)    NOT NULL,
  "image"       VARCHAR(100)   NOT NULL
);
CREATE TABLE "shop_product_categories" (
  "id"          SERIAL  NOT NULL PRIMARY KEY,
  "product_id"  INTEGER NOT NULL,
  "category_id" INTEGER NOT NULL
);
--
-- Add field product to cartitem
--
ALTER TABLE "shop_cartitem" ADD COLUMN "product_id" INTEGER NOT NULL;
ALTER TABLE "shop_cartitem" ALTER COLUMN "product_id" DROP DEFAULT;
ALTER TABLE "shop_cartitem" ADD CONSTRAINT "shop_cartitem_cart_id_6bf1447e_fk_shop_cart_id" FOREIGN KEY ("cart_id") REFERENCES "shop_cart" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "shop_cartitem_c44d83f7" ON "shop_cartitem" ("cart_id");
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categories_product_id_59c38762_fk_shop_product_id" FOREIGN KEY ("product_id") REFERENCES "shop_product" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categorie_category_id_7b004fe8_fk_shop_category_id" FOREIGN KEY ("category_id") REFERENCES "shop_category" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "shop_product_categories" ADD CONSTRAINT "shop_product_categories_product_id_edca6f84_uniq" UNIQUE ("product_id", "category_id");
CREATE INDEX "shop_product_categories_9bea82de" ON "shop_product_categories" ("product_id");
CREATE INDEX "shop_product_categories_b583a629" ON "shop_product_categories" ("category_id");
CREATE INDEX "shop_cartitem_9bea82de" ON "shop_cartitem" ("product_id");
ALTER TABLE "shop_cartitem" ADD CONSTRAINT "shop_cartitem_product_id_09e4b7dd_fk_shop_product_id" FOREIGN KEY ("product_id") REFERENCES "shop_product" ("id") DEFERRABLE INITIALLY DEFERRED;

COMMIT;
