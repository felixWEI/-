import sqlite3 as db

PATH=r'C:\Program Files (x86)\Thunder\Profiles\TaskDb.dat'
if __name__ == '__main__':
    # with open(PATH,'r') as fileObj:
    #     for eachLine in fileObj:
    #         print eachLine
    conn = db.connect(PATH)
    cursor = conn.cursor()
    #cursor.execute("select name from sqlite_master where type='table' order by name")
    cursor.execute("select * from AccelerateTaskMap218587198_superspeed_1_1")
    rows = cursor.fetchall()
    for eachLine in rows:
        #print type(eachLine)
        for eachItem in eachLine:
            if isinstance(eachItem,buffer):
                print len(eachItem)
                eachItem[127] = 1
            print eachItem
