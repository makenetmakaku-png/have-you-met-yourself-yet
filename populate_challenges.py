from database import conn, cursor

challenges = [
(1,"Sit somewhere with no phone and wait until your brain shuts up."),
(2,"Write one honest page you'd never show anyone."),
(3,"Walk with no destination and no audio. Just walk."),
(4,"Notice five things you've never looked at in your own home."),
(5,"Cook something slow. No recipe video. No multitasking."),
(6,"Sit on a bench and watch people without making it weird."),
(7,"Re-read something you wrote years ago. Try not to cringe."),
(8,"Say out loud the thing you've been avoiding."),
(9,"Clean one small area like it's the only thing that exists."),
(10,"Take photos of boring things that feel weirdly important."),
(11,"Sit in silence for ten minutes. Don't fix anything."),
(12,"Write down what actually matters to you. Not the résumé version."),
(13,"Listen to a song. Only listen."),
(14,"Rearrange a corner of your space until it feels like yours again."),
(15,"Go outside before most people are awake."),
]

cursor.executemany(
    "INSERT OR IGNORE INTO challenges(day,text) VALUES(?,?)",
    challenges
)

conn.commit()

print("Challenges imported!")