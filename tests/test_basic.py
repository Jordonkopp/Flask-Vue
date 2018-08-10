from server import db
from server.models.key import Key


# client passed from client - look into pytest for more info about fixtures
def test_get_user(client):
    rs = client.get("/keys")

    assert rs.status_code == 200
    ret_dict = rs.json  # gives you a dictionary
    assert ret_dict["success"] == True

    # create Person and test whether it returns a person
    temp_key = Key(key="123423")
    db.session.add(temp_key)
    db.session.commit()

    rs = client.get("/keys")
    rs_dict = rs.json
    assert len(rs_dict["result"]["keys"]) == 1
    assert rs_dict["result"]["keys"][0]["key"] == "123423"

    # TODO: Create proper tear down
    # Remove the created user
    db.session.delete(temp_key)
    db.session.commit()


# TODO: Expand test suite
