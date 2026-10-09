from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg://relay:relay@127.0.0.1:5432/relay",
    connect_args={"connect_timeout": 3},
)
