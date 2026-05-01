import psycopg2
from config import DB_CONFIG


def connect():
    # Connect to PostgreSQL
    return psycopg2.connect(**DB_CONFIG)


def create_tables():
    # Create players and game_sessions tables
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        create table if not exists players (
            id serial primary key,
            username varchar(50) unique not null
        );
    """)

    cur.execute("""
        create table if not exists game_sessions (
            id serial primary key,
            player_id int references players(id) on delete cascade,
            score int not null,
            level_reached int not null,
            played_at timestamp default now()
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def get_or_create_player(username):
    # Return player id. If player does not exist, create it.
    conn = connect()
    cur = conn.cursor()

    cur.execute("select id from players where username = %s", (username,))
    row = cur.fetchone()

    if row:
        player_id = row[0]
    else:
        cur.execute(
            "insert into players(username) values(%s) returning id",
            (username,)
        )
        player_id = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return player_id


def save_game(username, score, level):
    # Save game result after game over
    player_id = get_or_create_player(username)

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        insert into game_sessions(player_id, score, level_reached)
        values(%s, %s, %s)
    """, (player_id, score, level))

    conn.commit()
    cur.close()
    conn.close()


def get_top_players():
    # Top 10 scores for leaderboard screen
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        select p.username, g.score, g.level_reached, g.played_at
        from game_sessions g
        join players p on g.player_id = p.id
        order by g.score desc, g.level_reached desc
        limit 10
    """)

    rows = cur.fetchall()
    cur.close()
    conn.close()

    return rows


def get_best_score(username):
    # Personal best for current player
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        select max(g.score)
        from game_sessions g
        join players p on g.player_id = p.id
        where p.username = %s
    """, (username,))

    best = cur.fetchone()[0]

    cur.close()
    conn.close()

    return best if best else 0