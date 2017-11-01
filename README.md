# Webhook to save messages and respond automatically

Docker compose create:
 * Flask app (on port 5000): Communicate with rapidpro like kannel channel
 * Celery worker: Classify and send message like a common user
 * Flower interface:  Expose the queues and the workers
