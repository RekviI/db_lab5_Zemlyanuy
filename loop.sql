-- Loop for Laboratory №5
SELECT * FROM Person;
CREATE TABLE PersonCopy AS SELECT * FROM person; 
SELECT * FROM PersonCopy;
DELETE FROM PersonCopy;
DROP TABLE PersonCopy;

DO $$
 DECLARE
     user_id  personcopy.user_id%TYPE;
     age personcopy.age%TYPE;
	 gender personcopy.gender%TYPE;
-- На данний момент в нас з'являється нюанс який витік ще з 3 лабки, виправляти його буде дуже складно
-- бо треба перероблювати всю попередню роботу, але на диво воно не виконує subscription як окрему функцію
-- а взаємодіє з нею як з звичайним стовпцем, що можна побачити при виконанні звдання, тому ми його просто не чипаємо
	 subscription personcopy.subscription%TYPE; 

 BEGIN
     user_id := 1140;
     age := 11;
     FOR counter IN 1..20
         LOOP
            INSERT INTO personcopy(user_id, age, gender, subscription)
             VALUES (user_id || counter, age + counter, CASE WHEN counter % 2 = 1 THEN 'Male' ELSE 'Female' END,
					 CASE WHEN counter % 3 = 1 THEN 'Premium' ELSE 'Free' END);
         END LOOP;
 END;
 $$