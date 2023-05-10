from rabbitmq_consumer.subscriber import Subscriber

subscriber = Subscriber("topic_logs", "#")
subscriber.setup()