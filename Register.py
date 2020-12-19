from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from helpers import register_page_helper
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineIconListItem, OneLineListItem
from kivymd.uix.picker import MDDatePicker, MDTimePicker
from kivy.uix.popup import Popup
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton, MDRectangleFlatButton, MDFlatButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
import mysql.connector
import random

Window.size = (350, 550)
db = mysql.connector.connect(host="db4free.net", user="debasishdalei", passwd="Debasishdalei@1",
                             database="debasishdatabase")
tmp_cursor = db.cursor()

StaffID = ""
StaffName = ""
CLASS = ""
SUBJECT = ""
DATE = ""
TIME = ""
class_obj = None
subject_obj = None
date_obj = None
time_obj = None

sm = ScreenManager()


class RegisterScreen(Screen):
    pass


class StaffScreen(Screen):
    pass


class StudentScreen(Screen):
    pass


class StaffRegisterScreen(Screen):

    def on_enter(self, *args):
        query = "SELECT sid FROM staff_table"
        tmp_cursor.execute(query)
        result = tmp_cursor.fetchall()
        while True:
            tmp = random.randint(0, 100000)  # Un-Redundent values are not accepted
            flag = 1
            for x in result:
                if x[0] == tmp:
                    flag = 0
                    break
            if flag == 1:
                self.SID = tmp
                break
        self.ids.stf_sid.text = "SID " + str(self.SID) + " (Remember it for login)"

    def submit(self):
        query = "INSERT INTO staff_table VALUES (%s,%s,%s,%s,%s,%s)"
        val = (
            self.ids.stf_name.text,
            self.ids.stf_department.text,
            self.ids.stf_qualification.text,
            self.ids.stf_email.text,
            self.SID,
            self.ids.stf_password.text
        )
        tmp_cursor.execute(query, val)
        db.commit()


class StudentRegisterScreen(Screen):
    pass


class StaffLoginScreen(Screen):
    def submit(self):
        global StaffName
        global StaffID
        query = "SELECT * FROM staff_table WHERE sid = %s AND password = %s"
        val = (self.ids.stf_sid.text, self.ids.stf_password.text)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        if len(result) == 1:
            print("Welcome")
            StaffID = self.ids.stf_sid.text
            for x in result:
                StaffName = x[0]
            self.manager.current = 'staffhomescreen'
        else:
            popup = Popup(title='Error',
                          content=MDLabel(text="Incorrect credentials"),
                          size_hint=(None, None), size=(300, 100))
            popup.open()


class StudentLoginScreen(Screen):
    pass


class StaffHomeScreen(Screen):
    def on_enter(self, *args):
        global StaffName
        global class_obj
        global subject_obj
        global date_obj
        global time_obj
        self.ids.staff_name.text = StaffName
        class_obj = self.ids.class_tag
        subject_obj = self.ids.subject_tag
        date_obj = self.ids.date_tag
        time_obj = self.ids.time_tag

    def on_select_class(self):
        global StaffID

        class ClassList(OneLineIconListItem):
            def on_release(self):
                global CLASS
                global class_obj
                CLASS = self.text
                class_obj.text = "       Class(" + CLASS + ")"

        query = "SELECT DISTINCT class from staff_class WHERE sid = %s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        class_list = []
        for item in result:
            list_item = ClassList(text=item[0])
            class_list.append(list_item)
        dialog = MDDialog(size_hint_x=None, width=300, type='confirmation',
                          items=class_list)
        dialog.title = 'Select class'
        dialog.open()

    def on_select_subject(self):
        global StaffID

        class SubjectList(OneLineIconListItem):
            def on_release(self):
                global SUBJECT
                global subject_obj
                SUBJECT = self.text
                subject_obj.text = "       Subject(" + SUBJECT + ")"

        query = "SELECT DISTINCT subject from staff_class WHERE sid = %s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        subject_list = []
        for item in result:
            list_item = SubjectList(text=item[0])
            subject_list.append(list_item)
        dialog = MDDialog(size_hint_x=None, width=300, type='confirmation',
                          items=subject_list)
        dialog.title = 'Select subject'
        dialog.open()

    def on_select_date(self):
        MDDatePicker(self.set_date).open()

    def on_select_time(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.set_time)
        time_dialog.open()

    def set_date(self, date):
        global DATE
        global date_obj
        DATE = str(date)
        date_obj.text = "       Date(" + DATE + ")"

    def set_time(self, instance, time):
        global TIME
        global time_obj
        TIME = str(time)
        time_obj.text = "       Time(" + TIME + ")"

    def take_attendance(self):
        globals()
        sql = "select count(*) from staff_class where class=%s and subject=%s"
        val = (CLASS, SUBJECT)
        tmp_cursor.execute(sql, val)
        if tmp_cursor.fetchone()[0] > 0 and \
                len(CLASS) > 0 and len(SUBJECT) > 0 and len(DATE) > 0 and len(TIME) > 0:
            query = "SELECT cs_code FROM staff_class where sid=%s AND class=%s AND subject=%s"
            val = (StaffID, CLASS, SUBJECT)
            tmp_cursor.execute(query, val)
            code = tmp_cursor.fetchone()[0]
            query = "SELECT * FROM submission WHERE cs_code=%s AND date=%s AND time=%s"
            val = (code, DATE, TIME)
            tmp_cursor.execute(query, val)
            code = tmp_cursor.fetchall()
            if len(code) == 0:
                self.manager.current = 'attendancescreen'
            else:
                popup = Popup(title='Error',
                              content=MDLabel(text="Already recorded!!Please delete previous submission"),
                              size_hint=(None, None), size=(300, 100))
                popup.open()
        else:
            popup = Popup(title='Error',
                          content=MDLabel(text="Class and Subject doesn't match or select all four fields"),
                          size_hint=(None, None), size=(300, 100))
            popup.open()

    def on_leave(self, *args):
        globals()
        class_obj.text = "       Class?"
        subject_obj.text = "       Subject?"
        date_obj.text = "       Date?"
        time_obj.text = "       Time?"


class AttendanceScreen(Screen):
    def on_enter(self, *args):
        globals()
        self.ids.staff_name.text = StaffName
        self.ids.class_name.text = CLASS
        self.ids.subject_name.text = SUBJECT
        self.ids.date_name.text = DATE
        self.ids.time_name.text = TIME
        query = "SELECT cs_code FROM staff_class where sid=%s AND class=%s AND subject=%s"
        val = (StaffID, CLASS, SUBJECT)
        tmp_cursor.execute(query, val)
        self.code = tmp_cursor.fetchone()[0]
        query = "SELECT roll_no FROM student_class WHERE cs_code=%s"
        val = (self.code,)
        tmp_cursor.execute(query, val)
        self.roll_nos = []
        self.roll_nos_dict = {}
        for x in tmp_cursor.fetchall():
            self.roll_nos.append(x[0])
            bl = BoxLayout(orientation='horizontal', size_hint=(1, None), height=Window.height * 0.07)
            label = MDLabel(text=x[0], halign='center')
            cb1 = MDCheckbox(group=x[0], active=True)
            cb2 = MDCheckbox(group=x[0])
            tb = MDTextField()
            self.roll_nos_dict[x[0]] = [cb1, tb]
            bl.add_widget(label)
            bl.add_widget(cb1)
            bl.add_widget(cb2)
            bl.add_widget(tb)
            self.ids.list_of_students.add_widget(bl)

    def submit(self):
        global CLASS
        global SUBJECT
        global DATE
        global TIME
        for x in self.roll_nos:

            self.report = ""
            if self.roll_nos_dict[x][0].active:
                self.report = "P"
            else:
                self.report = "A"
            query = "INSERT INTO attendance VALUES(%s,%s,%s,%s,%s,%s)"
            val = (x, self.code, DATE, TIME, self.report, self.roll_nos_dict[x][1].text)
            tmp_cursor.execute(query, val)
            db.commit()

        query = "INSERT INTO submission VALUES(%s,%s,%s)"
        val = (self.code, DATE, TIME)
        tmp_cursor.execute(query, val)
        db.commit()
        popup = Popup(title='Submission',
                      content=MDLabel(text="Successfully recorded"), size_hint=(None, None), size=(300, 100))
        popup.open()
        self.manager.current = 'staffhomescreen'

    def on_leave(self, *args):
        global CLASS
        global SUBJECT
        global DATE
        global TIME
        CLASS = ""
        SUBJECT = ""
        DATE = ""
        TIME = ""
        self.ids.list_of_students.clear_widgets()


class AddClassScreen(Screen):
    def on_enter(self, *args):
        global StaffName
        self.ids.staff_name.text = StaffName
        self.roll_objs = []

    def make_list(self):
        obj = self.ids.student_list
        if len(self.ids.std_cnt.text) > 0:
            for i in range(0, int(self.ids.std_cnt.text)):
                item = MDTextField(mode='rectangle')
                self.roll_objs.append(item)
                obj.add_widget(item)

    def add(self):
        if len(self.ids.cls_name.text) == 0 or len(self.ids.sub_name.text) == 0 or len(self.ids.std_cnt.text) == 0:
            return
        global StaffID
        cls_name = self.ids.cls_name.text
        sub_name = self.ids.sub_name.text
        roll_nos = []
        for i in self.roll_objs:
            roll_nos.append(i.text)

        query = "SELECT cs_code FROM staff_class"
        tmp_cursor.execute(query)
        result = tmp_cursor.fetchall()
        while True:
            tmp = random.randint(100, 999)  # Un-Redundent values for CS_CODE
            flag = 1
            for x in result:
                if x[0] == tmp:
                    flag = 0
                    break
            if flag == 1:
                self.cs_code = tmp
                break
        query = "INSERT INTO staff_class VALUES(%s,%s,%s,%s)"
        val = (StaffID, cls_name, sub_name, self.cs_code)
        tmp_cursor.execute(query, val)
        db.commit()
        for i in roll_nos:
            query = "INSERT INTO student_class VALUES(%s,%s)"
            val = (self.cs_code, i)
            tmp_cursor.execute(query, val)
            db.commit()
        popup = Popup(title='Success',
                      content=MDLabel(text="New class added with id:" + str(self.cs_code)),
                      size_hint=(None, None), size=(300, 100))
        popup.open()
        self.manager.current = "staffhomescreen"

    def on_leave(self, *args):
        self.ids.student_list.clear_widgets()
        self.ids.cls_name.text = ""
        self.ids.sub_name.text = ""
        self.ids.std_cnt.text = ""


class EditClassScreen(Screen):
    def on_enter(self, *args):
        global StaffName
        self.ids.staff_name.text = StaffName
        query = "SELECT DISTINCT class,cs_code from staff_class WHERE sid = %s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        self.buttons_dict = {}
        for item in result:
            bl = BoxLayout(orientation='horizontal', size_hint=(1, None), height=Window.height * 0.1)
            label = MDLabel(text=item[0], halign='center')
            button1 = MDIconButton(icon='border-color', pos_hint={'center_x': 0.5})
            button1.bind(on_press=self.edit)
            self.buttons_dict[button1] = item[1]
            button2 = MDIconButton(icon='delete', pos_hint={'center_x': 0.5})
            button2.bind(on_press=self.delete)
            self.buttons_dict[button2] = item[1]
            bl.add_widget(label)
            bl.add_widget(button1)
            bl.add_widget(button2)
            self.ids.class_list.add_widget(bl)

    def edit(self, instance):
        global CLASS
        CLASS = self.buttons_dict[instance]
        self.manager.current = 'editscreen'

    def delete(self, instance):
        self.class_id = self.buttons_dict[instance]
        btn1 = MDRectangleFlatButton(text='Yes')
        btn1.bind(on_press=self.yes)
        btn2 = MDRectangleFlatButton(text='No')
        btn2.bind(on_press=self.no)
        self.dialog = MDDialog(title='Confirm', text='Are you sure?', size_hint_x=None, width=300, buttons=[btn1, btn2])
        self.dialog.open()

    def yes(self, instance):
        sql = "DELETE FROM staff_class where cs_code=%s"
        val = (self.class_id,)
        tmp_cursor.execute(sql, val)
        db.commit()
        sql = "DELETE FROM student_class where cs_code=%s"
        val = (self.class_id,)
        tmp_cursor.execute(sql, val)
        db.commit()
        sql = "DELETE FROM attendance where cs_code=%s"
        val = (self.class_id,)
        tmp_cursor.execute(sql, val)
        db.commit()
        self.dialog.dismiss()
        popup = Popup(title='Deleted',
                      content=MDLabel(text="Class id:" + self.class_id + " deleted successfully"),
                      size_hint=(None, None), size=(300, 100))
        popup.open()
        self.on_leave()
        self.on_enter()
        self.manager.current = 'editclassscreen'

    def no(self, instance):
        self.dialog.dismiss()

    def on_leave(self, *args):
        self.ids.class_list.clear_widgets()


class EditScreen(Screen):
    def on_enter(self, *args):
        global CLASS
        global StaffName
        self.flag = 1
        self.ids.staff_name.text = StaffName
        sql = "SELECT roll_no FROM student_class WHERE cs_code=%s"
        val = (CLASS,)
        tmp_cursor.execute(sql, val)
        result = tmp_cursor.fetchall()
        self.buttons_dict = {}
        for item in result:
            bl = BoxLayout(orientation='horizontal', size_hint=(1, None), height=Window.height * 0.1)
            label = MDLabel(text=item[0], halign='center')
            button = MDIconButton(icon='minus', pos_hint={'center_x': 0.1})
            button.bind(on_press=self.delete)
            self.buttons_dict[button] = item[0]
            bl.add_widget(label)
            bl.add_widget(button)
            self.ids.student_list.add_widget(bl)

    def delete(self, instance):
        global CLASS
        roll = self.buttons_dict[instance]
        sql = "DELETE FROM student_class WHERE cs_code=%s and roll_no=%s"
        val = (CLASS, roll,)
        tmp_cursor.execute(sql, val)
        db.commit()
        sql = "DELETE FROM attendance where cs_code=%s and roll_no=%s"
        val = (CLASS, roll,)
        tmp_cursor.execute(sql, val)
        db.commit()
        self.on_leave()
        self.on_enter()
        self.manager.current = 'editscreen'

    def add_student(self):
        if self.flag == 1:
            self.flag = 0
        else:
            return
        self.textbox = MDTextField(pos_hint={'center_y': 0.055})
        self.button = MDFlatButton(text='ADD', pos_hint={'center_y': 0.055})
        self.button.bind(on_press=self.add)
        self.ids.bottom_box.add_widget(self.textbox)
        self.ids.bottom_box.add_widget(self.button)

    def add(self, instance):
        if len(self.textbox.text) == 0:
            return
        global CLASS
        roll = self.textbox.text
        sql = "INSERT INTO student_class VALUES(%s,%s)"
        val = (CLASS, roll,)
        tmp_cursor.execute(sql, val)
        db.commit()
        self.ids.bottom_box.remove_widget(self.textbox)
        self.ids.bottom_box.remove_widget(self.button)
        self.on_leave()
        self.on_enter()
        self.manager.current = 'editscreen'

    def on_leave(self, *args):
        self.ids.student_list.clear_widgets()
        self.ids.bottom_box.remove_widget(self.textbox)
        self.ids.bottom_box.remove_widget(self.button)

class SubmissionScreen(Screen):
    def on_enter(self, *args):
        global StaffName
        global StaffID
        self.ids.staff_name.text = StaffName
        query = "SELECT cs_code FROM staff_class WHERE sid=%s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        self.codes = ""
        for x in result:
            self.codes += x[0] + ","
        self.codes = self.codes.strip(',')
        query = "SELECT * FROM submission WHERE cs_code IN(" + self.codes + ") ORDER BY date DESC,time DESC"
        tmp_cursor.execute(query)
        result = tmp_cursor.fetchall()
        table_rows = []
        for x in result:
            q = "SELECT class,subject FROM staff_class WHERE cs_code=%s"
            v = (x[0],)
            tmp_cursor.execute(q, v)
            r = tmp_cursor.fetchone()
            table_rows.append(
                (str(x[1]), str(x[2]), str(r[0]), str(r[1]), str(x[0])))  # date,time,class,subject,cs_code
        if len(table_rows) > 0:
            data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                     size_hint=(1, 1),
                                     check=True,
                                     rows_num=len(table_rows),
                                     column_data=[
                                         ("Date", dp(30)),
                                         ("Time", dp(15)),
                                         ("Class", dp(18)),
                                         ("Subject", dp(18)),
                                         ("Code", dp(15))
                                     ],
                                     row_data=table_rows
                                     )
            data_table.bind(on_check_press=self.check_press)
            self.ids.submission_list.add_widget(data_table)

    def check_press(self, instance_table, current_row):
        self.date = current_row[0]
        self.time = current_row[1]
        self.cs_code = current_row[4]
        report = ScrollView()
        query = "SELECT roll_no,report,remark FROM attendance WHERE cs_code=%s AND date=%s AND time=%s"
        val = (self.cs_code, self.date, self.time)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        mdlist = MDList()
        for item in result:
            bl = BoxLayout(orientation='horizontal', size_hint=(1, None), height=Window.height * 0.07)
            label1 = MDLabel(text=item[0], halign='center')
            label2 = MDLabel(text=item[1], halign='center')
            label3 = MDLabel(text=item[2], halign='center')
            bl.add_widget(label1)
            bl.add_widget(label2)
            bl.add_widget(label3)
            mdlist.add_widget(bl)
        report.add_widget(mdlist)

        del_btn = MDIconButton(icon='delete')
        del_btn.bind(on_press=self.del_submission)
        self.dialog = MDDialog(size_hint_x=None, width=300, type='custom',
                               content_cls=report, buttons=[del_btn])
        self.dialog.title = current_row[2] + "(" + current_row[3] + ")    Dt-" + self.date + " at " + self.time
        self.dialog.open()

    def del_submission(self, obj):
        query = "DELETE FROM submission WHERE cs_code=%s AND date=%s AND time=%s"
        val = (self.cs_code, self.date, self.time)
        tmp_cursor.execute(query, val)
        db.commit()
        query = "DELETE FROM attendance WHERE cs_code=%s AND date=%s AND time=%s"
        val = (self.cs_code, self.date, self.time)
        tmp_cursor.execute(query, val)
        db.commit()
        self.dialog.dismiss()
        self.on_leave()
        self.on_enter()

    def on_leave(self, *args):
        self.ids.submission_list.clear_widgets()


class ReportScreen(Screen):
    def on_enter(self, *args):
        global StaffID
        self.ids.staff_name.text = StaffName

    def on_select_class(self):
        global StaffID
        global class_obj
        class_obj = self.ids.class_label

        class ClassList(OneLineIconListItem):
            def on_release(self):
                global CLASS
                global class_obj
                CLASS = self.text
                class_obj.text = CLASS

        query = "SELECT DISTINCT class from staff_class WHERE sid = %s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        class_list = []
        for item in result:
            list_item = ClassList(text=item[0])
            class_list.append(list_item)
        dialog = MDDialog(size_hint_x=None, width=300, type='confirmation',
                          items=class_list)
        dialog.title = 'Select class'
        dialog.open()

    def on_select_subject(self):
        global StaffID
        global subject_obj
        subject_obj = self.ids.subject_label

        class SubjectList(OneLineIconListItem):
            def on_release(self):
                global SUBJECT
                global subject_obj
                SUBJECT = self.text
                subject_obj.text = SUBJECT

        query = "SELECT DISTINCT subject from staff_class WHERE sid = %s"
        val = (StaffID,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        subject_list = []
        for item in result:
            list_item = SubjectList(text=item[0])
            subject_list.append(list_item)
        dialog = MDDialog(size_hint_x=None, width=300, type='confirmation',
                          items=subject_list)
        dialog.title = 'Select subject'
        dialog.open()

    def show_stats(self):
        global StaffID
        global CLASS
        global SUBJECT
        query = "SELECT cs_code FROM staff_class WHERE sid=%s and class=%s and subject=%s"
        val = (StaffID, CLASS, SUBJECT,)
        tmp_cursor.execute(query, val)
        result = tmp_cursor.fetchall()
        if len(result) == 1:
            cs_code = result[0][0]
            print(cs_code)
            table_rows = [["Aug", 100, 80], ["Sep", 100, 80], ["Oct", 100, 80], ["Nov", 100, 80], ["Dec", 100, 80],
                          ["Jan", 100, 80]]
            data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.4},
                                     size_hint=(1, 1),
                                     rows_num=6,
                                     column_data=[
                                         ("Month", dp(20)),
                                         ("Total Classes", dp(30)),
                                         ("Present", dp(20)),
                                     ],
                                     row_data=table_rows
                                     )
            self.ids.report_board.add_widget(data_table)


sm.add_widget(RegisterScreen(name='registerscreen'))
sm.add_widget(StaffScreen(name='staffscreen'))
sm.add_widget(StudentScreen(name='studentscreen'))
sm.add_widget(StaffRegisterScreen(name='staffregisterscreen'))
sm.add_widget(StudentRegisterScreen(name='studentregisterscreen'))
sm.add_widget(StaffLoginScreen(name='staffloginscreen'))
sm.add_widget(StudentLoginScreen(name='studentloginscreen'))
sm.add_widget(StaffHomeScreen(name='staffhomescreen'))
sm.add_widget(AttendanceScreen(name='attendancescreen'))
sm.add_widget(AddClassScreen(name='addclassscreen'))
sm.add_widget(EditClassScreen(name='editclassscreen'))
sm.add_widget(EditScreen(name='editscreen'))
sm.add_widget(SubmissionScreen(name='submissionscreen'))
sm.add_widget(ReportScreen(name='reportscreen'))


class JobHub(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Cyan'
        screen = Builder.load_string(register_page_helper)
        return screen


JobHub().run()
