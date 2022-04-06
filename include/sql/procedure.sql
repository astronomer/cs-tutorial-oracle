CREATE PROCEDURE remove_prod (product_id INTEGER) AS
   tot_prod NUMBER;
   BEGIN
      DELETE FROM product
      WHERE product.product_id = remove_prod.product_id;
   tot_prod := tot_prod - 1;
   END;