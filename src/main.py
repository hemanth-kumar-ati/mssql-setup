from config.database import create_db_engine, test_connection, get_database_names, Base
from models import User
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine (which also initializes tables)
    engine = create_db_engine()
    
    print("Testing connection...")
    print(test_connection(engine))
    
    # Create session factory
    SessionLocal = sessionmaker(bind=engine)
    scores = {"math": 90, "science": 85}
    movies_watched = ["Inception", "The Matrix"]
    # Use session with context manager
    with SessionLocal() as session:
        try:
            # Create some sample users
            users_data = [
                {"Name": "John Doe", "Email": "john@example.com"},
                {"Name": "Jane Smith", "Email": "jane@example.com"},
                {"Name": "Bob Johnson", "Email": "bob@example.com"},
                {"Name": "Alice Brown", "Email": "alice@example.com", "scores": scores, "movies_watched": movies_watched},
                {"Name": "Charlie Black", "Email": "black@example.com", "scores": scores, "movies_watched": movies_watched},
            ]
            
            # Add users
            for user_data in users_data:
                # Check if user already exists
                existing_user = session.query(User).filter_by(Email=user_data["Email"]).first()
                if not existing_user:
                    new_user = User(**user_data)
                    session.add(new_user)
                    print(f"Adding user: {user_data['Name']}")
                else:
                    print(f"User with email {user_data['Email']} already exists")
            
            # Commit the transactions
            session.commit()
            
            # Query all users
            print("\nAll users in database:")
            users = session.query(User).all()
            for user in users:
                print(f"ID: {user.Id}, Name: {user.Name}, Email: {user.Email}, scores:{user.scores}, movies_watched:{user.movies_watched}")
            
            # Query specific user
            print("\nQuerying for user with email 'john@example.com':")
            john = session.query(User).filter_by(Email="john@example.com").first()
            if john:
                print(f"Found user: ID: {john.Id}, Name: {john.Name}, Email: {john.Email}")
            print("Good to go!")
                
        except Exception as e:
            print(f"Error: {str(e)}")
            session.rollback()
            raise