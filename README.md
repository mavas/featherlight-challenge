# Featherlight challenge

Looks like one might want to use a tool like curl to test the server:

```
curl -XPOST -d "{'Shift': 2, 'Message': 'I love you'}" --header "Content-type: application/json"
curl -XPOST --data '{"temp": 2}' localhost:23456/api/encode/ --header "Content-type: application/json"
curl -XPOST --data '{"Shift": 2, "Message": "love"}' localhost:23456/api/encode/ --header "Content-type: application/json"
```
