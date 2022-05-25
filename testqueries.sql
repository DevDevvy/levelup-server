SELECT * FROM levelupapi_game_type;

SELECT * FROM auth_user;
SELECT * FROM authtoken_token;
SELECT * FROM levelupapi_gamer;

SELECT * FROM levelupapi_event;

SELECT * FROM levelupapi_game_type;

SELECT g.*, gr.user_id, a.first_name ||' '|| a.last_name AS FullName
            FROM levelupapi_Game g
            JOIN levelupapi_Gamer gr
                ON g.gamer_id = gr.id
            JOIN auth_user a
                ON a.id = gr.user_id

SELECT e.*, g.id AS gamer_id, a.first_name ||' '|| a.last_name AS full_name, gm.title
    FROM levelupapi_event e
    JOIN levelupapi_game gm
        ON e.game_id = gm.id
    JOIN levelupapi_gamer g
        ON e.organizer_id = g.id
    JOIN auth_user a 
        ON g.user_id = a.id