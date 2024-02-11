from datetime import date

import cv2
import sqlite3

camera_id = 0
delay = 1
window_name = 'Hack Club Member Scanner'

qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)

while True:
    ret, frame = cap.read()

    if ret:
        ret_qr, decoded_info, points, _ = qcd.detectAndDecodeMulti(frame)
        if ret_qr:
            for s, p in zip(decoded_info, points):
                if s:
                    conn = sqlite3.connect('members.db')
                    c = conn.cursor()
                    # check if the member is in the database
                    member = c.execute(f'''SELECT * FROM member WHERE id = {s} ''')
                    member = member.fetchone()
                    if member:
                        # show the member's name at scanning screen
                        cv2.putText(frame, member[1], (int(p[0][0]), int(p[0][1])), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (0, 255, 0), 2, cv2.LINE_AA)
                        current_date = date.today().strftime('%Y%m%d')
                        c.execute("UPDATE member SET date = ? WHERE id = ?", (current_date, s))
                        conn.commit()
                        conn.close()
                    else:
                        print(f'Unknown member {s}')
                    color = (0, 255, 0)
                else:
                    color = (0, 0, 255)
                frame = cv2.polylines(frame, [p.astype(int)], True, color, 8)
        cv2.imshow(window_name, frame)

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cv2.destroyWindow(window_name)