/*
a) actor id first_name last_name last_update
b)film_id title description release_year language_id original_language_id rental_rate length replacement_cost rating special_features last_update rental_duration
c) no other table contain actor_id or film_id
d) rental_id rental_date inventory_id customer_id return_date staff_id last_update rental
e)inventory include inventory_id film_id store_id last_update 
f)to understand naames, we can use inventory and rental table becouse thy contain information like names and all inventory trackings
*/

SELECT rental_date, inventory_id
FROM rental;

SELECT inventory_id, film_id
FROM inventory;

SELECT film_id, title
FROM film;

SELECT actor_id, first_name 
FROM actor;