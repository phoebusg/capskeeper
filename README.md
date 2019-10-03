# capskeeper
# Since Apple changed how caps lock behavior works while switching languages, Capskeeper script is again needed.

This is a simple script, so that we can keep the CAPS LOCK status while switching languages with the CMD+Space keys, in OS X. (as many people ask, "Caps Lock is turned off when I change the language, what can I do"
It uses the pyxhook module to listen to the key presses even in the background (included), and it also takes advantage of the pyautogui library to automatically press CAPS LOCK button, if needed (needs to be installed separatelly, with the command pip install -U pyautogui).

INSTALLATION INSTRUCTIONS - USAGE:
1. Install Python. Normally, it should be already installed, however if not, install Python3.

2. pyautogui librery is needed as well.
In terminal, type pip install -U pyautogui .

3. Download the script in your home folder:
cd ~
git clone git://github.com/phoebusg/capskeeper
This will create a folder named /capskeeper in your home folder, containing the script.

4. Run it!
cd capskeeper
python capskeeper_1.py

That's it! If you test it and it is OK, and if you want to keep using it by running it on the backgroung, then you can:
Close the terminal running the script, and force it to quit.
Then open a new terminal, and type:
  nohup python ~/capskeeper/capskeeper_1.py &
Don't forget the "&" in the end, in order to put it in the background!
You can now close the terminal, and the script will keep working.

If you want to run it on the background automatically every time you start your computer, you can add it with the Startup Applications app, from the Dash.
In Name field: Whatever you want.
Command field: /usr/bin/python /home/"username"/capskeeper/capskeeper_1.py &
Press save!
Now the script will run, every time you log in, automatically!


Ελληνικά

Πρόκειται για ένα απλό script γραμμένο σε Python, για να κρατάει την κατάσταση των κεφαλαίων
(CAPS LOCK) κατά την εναλλαγή γλώσσας, παρακάμπτωντας ένα bug σε συστήματα Ubuntu Unity
(σε άλλα γραφικά περιβάλλοντα, όπως mate, gnome shell κλπ, δεν έχει αναφερθεί κάτι τέτοιο).
Η λειτουργία του έχει σχεδιαστεί για χρήση με τον συνδιασμό Alt+Shift_L.
Αυτό που κάνει, είναι να παρακολουθεί το πληκτρολόγιο (ΜΗΝ ανησυχείτε, δεν θα στείλει τίποτα δεδομένα
πουθενά, απλά πρέπει να ξέρει πότε θα πατηθεί το Shift_L που αλλάζει την γλώσσα! Δείτε τον κώδικα.), 
και όταν πατηθεί το Shift_L τσεκάρει την κατάσταση του Caps Lock.
Όταν αφεθεί, την ξανατσεκάρει. Αν η κατάσταση έχει αλλάξει (ήταν ΚΕΦΑΛΑΙΑ και γύρισε σε πεζά), 
τότε στέλνει μια εντολή να πατηθεί το CAPS LOCK, οπότε ξαναγίνονται ΚΕΦΑΛΑΙΑ. 
Αν δεν έχει αλλάξει, δεν κάνει τίποτα.
Κατά την διάρκεια λειτουργίας του, δίνονται πληροφορίες για το τι κάνει, στην οθόνη.

OΔΗΓΙΕΣ ΕΓΚΑΤΑΣΤΑΣΗΣ& ΧΡΗΣΗΣ:
1. 	Εγκαθιστούμε την Python. Συνήθως, βρίσκεται ήδη εγκατεστημένη σε ένα linux σύστημα, 
	σε περίπτωση που δεν είναι, ανοίγουμε ένα τερματικό και γράφουμε την εντολή
	sudo apt install python.
2.	Θα χρειαστούμε την βιβλιοθήκη της python, pyautogui.
	Στο ίδιο τερματικό, πληκτρολογούμε:
	pip install -U pyautogui.
3.	Κατεβάζουμε το σκριπτ στον τοπικό μας φάκελο:
	cd ~
	git clone git://github.com/phoebusg/capskeeper
	Θα δημιουργηθεί ένας φάκελος, ο οποίος θα περιέχει το script.
4.	Το τρέχουμε!
	cd capskeeper
	python capskeeper_1.py

Αυτό ήταν! Κάντε δοκιμή, πατώντας caps lock και δοκιμάζοντας να αλλάξετε γλώσσες με Alt+Shift,
αν κρατάει τα κεφαλαία!

Σε περίπτωση που σας δουλεύει σωστά, και θέλετε να το αφήσετε να τρέχει στο παρασκήνιο:
Κλείνετε το προηγούμενο τερματικό, τερματίζοντας και την λειτουργία του script.
Ανοίγετε νέο τερματικό, και γράφετε:

	nohup python ~/capskeeper/capskeeper_1.py &

Μην ξεχάσετε το & στο τέλος, για να τρέξει στο παρασκήνιο!
Κλείνετε το τερματικό, και το script συνεχίζει να τρέχει.

Αν θέλετε να ξεκινά αυτόματα σε μόνιμη βάση, μπορείτε πολύ εύκολα, από την εφαρμογή 
"Προγράμματα εκκίνησης" του Ubuntu.
Πατάτε "Προσθήκη".
Και στα πεδία, βάζετε:
Όνομα: Ότι θέλετε...
Εντολή: /usr/bin/python /home/"username"/capskeeper/capskeeper_1.py &
Σχόλιο: Τίποτα

Πατάτε "Αποθήκευση".

Πλέον, το πρόγραμμα θα εκκινεί στο παρασκήνιο, κάθε φορά που θα εκκινεί ο λογαριασμός σας.
Κατά περίπτωση, μπορεί να χρειαστεί να αλλάξετε τις διαδρομές, αν δεν χρησιμοποιήσετε τις
ίδιες με αυτές του παραδείγματος.
