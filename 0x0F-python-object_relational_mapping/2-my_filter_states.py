#!/usr/bin/python3
""" display all values where name matches the argument"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                        port=3306,
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3])
    cur = db.cursor()
    cur.excute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
            ORDER BT states.id ASC".format(sys.argv[4]))
    rows = db.cursor()
    for row in rows:
        print(row)
