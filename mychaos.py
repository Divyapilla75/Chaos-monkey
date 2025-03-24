import socket
import time
#import psycopg2

def induce_disconnection(db_host, db_port, db_name, db_user, db_password, duration):
    # Create a connection to the PostgreSQL database
    conn = psycopg2.connect(
        host=postgres
        port=5243,
        database=apigee_x_db,
        user=postgres,
        password=root
    )

    # Get the socket associated with the connection
    db_socket = conn.get_backend_pid()

    conn.close()

    # Induce disconnection by closing the Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((db_host, db_port))

    # Wait for some time to maintain the disconnection
    print("Inducing disconnection to the database...")
    time.sleep(duration)

    # Close the socket to simulate a disconnection
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
    print(f"Disconnection induced for {duration} seconds.")

def restore_connection(db_host, db_port, db_name, db_user, db_password):
    # Normally, there's nothing to do here unless you need to reset some state.
    print("Restoring database connection (this would typically be handled by the application).")

