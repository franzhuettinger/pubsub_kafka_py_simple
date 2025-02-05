from confluent_kafka import Consumer

def main():
    # Create a consumer instance
    consumer = Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    # Subscribe to the topic 'new_topic_01'
    consumer.subscribe(['new_topic_01'])

    while True:
        # Poll for messages
        msg = consumer.poll(timeout=1.0)
    
        # If no message is received, continue
        if msg is None:
            continue

        # If an error is encountered, print the error and break the loop
        if msg.error():
            # Ignore EOF errors
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break
    
        # Print the received message
        print(f'Received message: {msg.value().decode('utf-8')} | Key={msg.key()} | Partition={msg.partition() } | Offset={msg.offset()} | Timestamp={msg.timestamp()}')

    # Close the consumer
    consumer.close()

if __name__ == "__main__":
    main()