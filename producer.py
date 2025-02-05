import time
from confluent_kafka import Producer

def delivery_callback(err, msg):
    """
    Called once for each message produced to indicate delivery result.
    """
    if err:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message produced: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def main():
    # Create a producer instance
    producer = Producer({
        'bootstrap.servers': 'localhost:9092'
        })
    
    num_iterations = 1000000 # Number of messages to produce

    for i in range(num_iterations):
        # Poll for events and call the delivery callback for each message
        producer.poll(0)

        # Produce a message
        msg = f'Hello, World! ({time.time()})'

        # Publish the message to the topic
        producer.produce('new_topic_01', msg.encode('utf-8'), callback=delivery_callback)
        
        # Wait for 10 ms
        time.sleep(0.01)

    # Wait until all messages are delivered
    producer.flush()

if __name__ == "__main__":
    main()
