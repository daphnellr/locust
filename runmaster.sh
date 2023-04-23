export PYTHONPATH=${PYTHONPATH}:`pwd`
python3 locust -f examples/basic.py --master --web-port 8082