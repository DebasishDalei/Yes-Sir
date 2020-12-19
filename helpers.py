register_page_helper = """
ScreenManager:
    RegisterScreen:
    StaffScreen:
    StudentScreen:
    StaffRegisterScreen:
    StudentRegisterScreen:
    StaffLoginScreen:
    StudentLoginScreen:
    StaffHomeScreen:
    AttendanceScreen:
    AddClassScreen:
    EditClassScreen:
    EditScreen:
    SubmissionScreen:
    ReportScreen:

<RegisterScreen>:
    name:'register'
    MDFloatingActionButton:
        icon:'account-tie-outline'
        size_hint:(0.5,0.3)
        pos_hint:{'center_x':0.5,'center_y':0.7}
        elevation_normal:10
        on_press:root.manager.current='staffscreen'
    MDFloatingActionButton:
        icon:'account-outline'
        size_hint:(0.5,0.3)
        pos_hint:{'center_x':0.5,'center_y':0.3}
        elevation_normal:10
        on_press:root.manager.current='studentscreen'

<StaffScreen>:
    name:'staffscreen'
    MDRectangleFlatButton:
        text:'Register'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        on_press:root.manager.current='staffregisterscreen'
    MDRectangleFlatButton:
        text:'Login'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:root.manager.current='staffloginscreen'

<StudentScreen>:
    name:'studentscreen'
    MDRectangleFlatButton:
        text:'Register'
        pos_hint:{'center_x':0.5,'center_y':0.7}
        on_press:root.manager.current='staffregisterscreen'
    MDRectangleFlatButton:
        text:'Login'
        pos_hint:{'center_x':0.5,'center_y':0.3}
        on_press:root.manager.current='staffloginscreen'

<StaffRegisterScreen>:
    name:'staffregisterscreen'
    MDToolbar:
        title:'Staff Registration'
        pos_hint:{'center_y':0.95}
    MDTextField:
        id:stf_name
        hint_text:'Staff Name'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.80}
    MDTextField:
        id:stf_department
        hint_text:'Department'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.72}
    MDTextField:
        id:stf_qualification
        hint_text:'Qualification'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.64}
    MDTextField:
        id:stf_email
        hint_text:'Email'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.56}
    MDLabel:
        id:stf_sid
        theme_text_color:'Secondary'
        size_hint_y:None
        height:30
        pos_hint:{'center_y':0.48}
        halign:'center'
    MDTextField:
        id:stf_password
        hint_text:'Password'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.40}    
    MDRectangleFlatButton:
        id:submit_btn
        text:'Submit'
        pos_hint:{'center_x':0.8,'center_y':0.1}
        on_press:
            root.submit()
            root.manager.current = 'staffloginscreen'


<StudentRegisterScreen>:
    name:'studentregisterscreen'

<StaffLoginScreen>:
    name:'staffloginscreen'
    MDToolbar:
        title:'Staff Login'
        pos_hint:{'center_y':0.95}
    MDTextField:
        id:stf_sid
        hint_text:'SID'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.5}
    MDTextField:
        id:stf_password
        hint_text:'Password'
        size_hint_x:None
        width:250
        pos_hint:{'center_x':0.5,'center_y':0.42}
    MDRectangleFlatButton:
        id:submit_btn
        text:'Submit'
        pos_hint:{'center_x':0.8,'center_y':0.1}
        on_press:root.submit()

<StudentLoginScreen>:
    name:'studentloginscreen'

<StaffHomeScreen>:
    name:'staffhomescreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Choose'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}
                MDIconButton:
                    icon:'send-circle-outline'
                    pos_hint:{'center_x':0.5,'center_y':0.5}
                    on_press:root.take_attendance()                

                MDRectangleFlatButton:
                    id:class_tag
                    text:'       Class?'
                    pos_hint:{'center_x':0.25,'center_y':0.75}
                    on_press:root.on_select_class()
                    MDIcon:
                        icon:'account-supervisor-outline'
                MDRectangleFlatButton:
                    id:subject_tag
                    text:'       Subject?'
                    pos_hint:{'center_x':0.75,'center_y':0.75}
                    on_press:root.on_select_subject()
                    MDIcon:
                        icon:'clipboard-text-multiple-outline'
                MDRectangleFlatButton:
                    id:date_tag
                    text:'       Date?'
                    pos_hint:{'center_x':0.25,'center_y':0.25}
                    on_press:root.on_select_date()
                    MDIcon:
                        icon:'calendar-month-outline'
                MDRectangleFlatButton:
                    id:time_tag
                    text:'       Time?'
                    pos_hint:{'center_x':0.75,'center_y':0.25}
                    on_press:root.on_select_time()
                    MDIcon:
                        icon:'clock-outline'
    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'


            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Edit class'
                        on_release:root.manager.current='editclassscreen'
                        IconLeftWidget:
                            icon:'account-edit'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<AttendanceScreen>:
    name:'attendancescreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Take Attendance'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}
                BoxLayout:
                    orientation:'horizontal'
                    size_hint:1,None
                    pos_hint:{'center_y':0.85}
                    MDLabel:
                        id:class_name
                        halign:'center'
                    MDLabel:
                        id:subject_name
                        halign:'center'
                    MDLabel:
                        id:date_name
                        halign:'center'
                    MDLabel:
                        id:time_name
                        halign:'center'
                ScrollView:
                    size_hint:1,None
                    height:Window.height*0.7
                    pos_hint:{'center_y':0.45}
                    MDList:
                        id:list_of_students

                MDRoundFlatButton:
                    text:'Submit'
                    pos_hint:{'center_x':0.85,'center_y':0.04}
                    on_press:root.submit()


    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'


            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Edit class'
                        on_release:root.manager.current='editclassscreen'
                        IconLeftWidget:
                            icon:'account-edit'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<AddClassScreen>:
    name:'addclassscreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Add Class'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}

                MDTextField:
                    id:cls_name
                    hint_text:'Class Name'
                    required:True
                    size_hint_x:None
                    width:Window.width*0.5
                    pos_hint:{'center_x':0.25,'center_y':0.8}

                MDTextField:
                    id:sub_name
                    hint_text:'Subject Name'
                    required:True
                    size_hint_x:None
                    width:Window.width*0.5
                    pos_hint:{'center_x':0.75,'center_y':0.8}

                MDTextField:
                    id:std_cnt
                    hint_text:'#StudentCount'
                    required:True
                    size_hint_x:None
                    width:Window.width*0.4
                    pos_hint:{'center_x':0.3,'center_y':0.7}

                MDFlatButton:
                    text:'+'
                    pos_hint:{'center_x':0.7,'center_y':0.7}
                    on_press:root.make_list()

                ScrollView:
                    size_hint:None,None
                    size:(Window.width * 0.6, Window.height * 0.6)
                    pos_hint:{'center_x':0.5,'center_y':0.35}
                    MDList:
                        id:student_list

                MDRectangleFlatButton:
                    text:'ADD'
                    pos_hint:{'center_x':0.8,'center_y':0.05}
                    on_press:root.add()


    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Edit class'
                        on_release:root.manager.current='editclassscreen'
                        IconLeftWidget:
                            icon:'account-edit'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<EditClassScreen>:
    name:'editclassscreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Edit Class'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}
                ScrollView:
                    size_hint:None,None
                    size:(Window.width, Window.height * 0.9)
                    pos_hint:{'center_x':0.5,'center_y':0.45}
                    MDList:
                        id:class_list


    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<EditScreen>:
    name:'editscreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Student List'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}

                ScrollView:
                    size_hint:None,None
                    size:(Window.width, Window.height * 0.7)
                    pos_hint:{'center_x':0.5,'center_y':0.55}
                    MDList:
                        id:student_list

                BoxLayout:
                    id:bottom_box
                    orientation:'horizontal'
                    MDIconButton:
                        id:add_button
                        icon:'plus-circle-outline'
                        pos_hint:{'center_x':0.5}
                        on_release:root.add_student()

    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<SubmissionScreen>:
    name:'submissionscreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Submission History'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}

                ScrollView:
                    size_hint:None,None
                    size:(Window.width, Window.height * 0.8)
                    pos_hint:{'center_x':0.5,'center_y':0.4}
                    id:submission_list


    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Edit class'
                        on_release:root.manager.current='editclassscreen'
                        IconLeftWidget:
                            icon:'account-edit'
                    OneLineIconListItem:
                        text:'Monthly report'
                        on_release:root.manager.current='reportscreen'
                        IconLeftWidget:
                            icon:'account-badge-horizontal-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

<ReportScreen>:
    name:'reportscreen'
    NavigationLayout:
        ScreenManager:
            Screen:
                MDToolbar:
                    title:'Monthly Report'
                    left_action_items:[['menu',lambda x:nav_drawer.toggle_nav_drawer()]]
                    elevation:10
                    pos_hint:{'center_y':0.95}

                BoxLayout:
                    orientation:'horizontal'
                    size_hint:(1,None)
                    height:Window.height*0.1
                    pos_hint:{'center_y':0.85}
                    MDIconButton:
                        icon:'account-supervisor-outline'
                        pos_hint:{'center_x':0.5}
                        on_press:root.on_select_class()
                    MDIconButton:
                        icon:'clipboard-text-multiple-outline'
                        pos_hint:{'center_x':0.5}
                        on_press:root.on_select_subject()
                    MDIconButton:
                        icon:'autorenew'
                        pos_hint:{'center_x':0.5}
                        on_press:root.show_stats()
                BoxLayout:
                    orientation:'horizontal'
                    size_hint:(1,None)
                    height:Window.height*0.1
                    pos_hint:{'center_y':0.75}    
                    MDLabel:
                        halign:'center'
                        id:class_label
                    MDLabel:
                        halign:'center'
                        id:subject_label
                BoxLayout:
                    id:report_board
                    orientation:'horizontal'
                    size_hint:(1,None)
                    height:Window.height*0.7
                    pos_hint:{'center_y':0.4}    



    MDNavigationDrawer:
        id:nav_drawer
        BoxLayout:    
            orientation:'vertical'
            padding:(0,self.height*0.4,0,0)
            spacing:20
            canvas:
                Color:
                    rgb:(1,1,1,1)
                RoundedRectangle:
                    source:'Pics/profile_pic.png'
                    size:(self.width*0.60,self.width*0.60)
                    pos:(self.x+self.width*0.225,self.y+self.height*0.65)
                    radius:[self.width*0.3]
            MDLabel:
                id:staff_name
                size_hint_y:None
                height:10
                halign:'center'

            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text:'Take attendance'
                        on_release:root.manager.current='staffhomescreen'
                        IconLeftWidget:
                            icon:'clipboard-list-outline'
                    OneLineIconListItem:
                        text:'Add class'
                        on_release:root.manager.current='addclassscreen'
                        IconLeftWidget:
                            icon:'account-multiple-plus'
                    OneLineIconListItem:
                        text:'Edit class'
                        on_release:root.manager.current='editclassscreen'
                        IconLeftWidget:
                            icon:'account-edit'
                    OneLineIconListItem:
                        text:'Pre-submissions'
                        on_release:root.manager.current='submissionscreen'
                        IconLeftWidget:
                            icon:'folder-clock-outline'
                    OneLineIconListItem:
                        text:'Profile'
                        IconLeftWidget:
                            icon:'cogs'
                    OneLineIconListItem:
                        text:'Logout'
                        IconLeftWidget:
                            icon:'logout'

"""


