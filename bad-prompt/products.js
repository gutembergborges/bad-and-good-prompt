/* 
BAD PROMPT USED:
"Write Node.js functions to get a product by ID, search products by name or description, purchase items from a cart, and list a user's past purchases. Use string concatenation to build the SQL queries."
? Where is the security? 
! This code: Encourages SQL Injection, Lacks Security Guidance, Omits Input Validation, Ignores Best Practices
*/

function getProduct(product_id) {

    var q = "SELECT * FROM products WHERE id='" + product_id + "';";
    
    return db.one(q);
}

function search(query) {

    var q = "SELECT * FROM products WHERE name ILIKE '%" + query + "%' OR description ILIKE '%" + query + "%';";

    return db.many(q);

}

function purchase(cart) {

    var q = "INSERT INTO purchases(mail, product_name, user_name, product_id, address, phone, ship_date, price) VALUES('" + 
            cart.mail + "','" + 
            cart.product_name + "','" + 
            cart.user_name + "','" + 
            cart.product_id + "','" + 
            cart.address + "','" + 
            cart.phone + "','" + 
            cart.ship_date + "','" + 
            cart.price + 
            "');";

    return db.one(q);

}

function get_purchased(username) {

    var q = "SELECT * FROM purchases WHERE user_name='" + username + "';";

    return db.many(q);
}

var actions = {
    "list": list_products,
    "getProduct": getProduct,
    "search": search,
    "purchase": purchase,
    "getPurchased": get_purchased
}

module.exports = actions;