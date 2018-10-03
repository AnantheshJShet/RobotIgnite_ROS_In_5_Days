{"filter":false,"title":"move_drone_square.py","tooltip":"/exercise_413/src/move_drone_square.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":["m"],"id":847}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":["e"],"id":848}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":["n"],"id":849}],[{"start":{"row":44,"column":51},"end":{"row":44,"column":52},"action":"remove","lines":["t"],"id":850}],[{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"remove","lines":["s"],"id":851}],[{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"remove","lines":["s"],"id":852}],[{"start":{"row":44,"column":49},"end":{"row":44,"column":50},"action":"insert","lines":["e"],"id":853}],[{"start":{"row":44,"column":50},"end":{"row":44,"column":51},"action":"insert","lines":["s"],"id":854}],[{"start":{"row":46,"column":23},"end":{"row":46,"column":31},"action":"remove","lines":["Stopping"],"id":855},{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"insert","lines":["T"]}],[{"start":{"row":46,"column":24},"end":{"row":46,"column":25},"action":"insert","lines":["u"],"id":856}],[{"start":{"row":46,"column":25},"end":{"row":46,"column":26},"action":"insert","lines":["r"],"id":857}],[{"start":{"row":46,"column":26},"end":{"row":46,"column":27},"action":"insert","lines":["n"],"id":858}],[{"start":{"row":46,"column":27},"end":{"row":46,"column":28},"action":"insert","lines":["i"],"id":859}],[{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"insert","lines":["n"],"id":860}],[{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"insert","lines":["g"],"id":861}],[{"start":{"row":48,"column":35},"end":{"row":48,"column":36},"action":"remove","lines":["0"],"id":862}],[{"start":{"row":48,"column":35},"end":{"row":48,"column":36},"action":"insert","lines":["1"],"id":863}],[{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"remove","lines":["p"],"id":864}],[{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"remove","lines":["o"],"id":865}],[{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"remove","lines":["t"],"id":866}],[{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"remove","lines":["s"],"id":867}],[{"start":{"row":45,"column":8},"end":{"row":45,"column":9},"action":"insert","lines":["t"],"id":868}],[{"start":{"row":45,"column":9},"end":{"row":45,"column":10},"action":"insert","lines":["u"],"id":869}],[{"start":{"row":45,"column":10},"end":{"row":45,"column":11},"action":"insert","lines":["r"],"id":870}],[{"start":{"row":45,"column":11},"end":{"row":45,"column":12},"action":"insert","lines":["n"],"id":871}],[{"start":{"row":49,"column":52},"end":{"row":56,"column":52},"action":"insert","lines":["","    ","    # Function that makes the drone turn 90 degrees","    def turn_drone(self):","        rospy.loginfo(\"Turning...\")","        self._move_msg.linear.x = 0.0","        self._move_msg.angular.z = 1.0","        self.publish_once_in_cmd_vel(self._move_msg)"],"id":872}],[{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"remove","lines":["n"],"id":873}],[{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"remove","lines":["r"],"id":874}],[{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"remove","lines":["u"],"id":875}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"remove","lines":["t"],"id":876}],[{"start":{"row":52,"column":8},"end":{"row":52,"column":9},"action":"insert","lines":["m"],"id":877}],[{"start":{"row":52,"column":9},"end":{"row":52,"column":10},"action":"insert","lines":["o"],"id":878}],[{"start":{"row":52,"column":10},"end":{"row":52,"column":11},"action":"insert","lines":["v"],"id":879}],[{"start":{"row":52,"column":11},"end":{"row":52,"column":12},"action":"insert","lines":["e"],"id":880}],[{"start":{"row":52,"column":12},"end":{"row":52,"column":13},"action":"insert","lines":["_"],"id":881}],[{"start":{"row":52,"column":13},"end":{"row":52,"column":14},"action":"insert","lines":["f"],"id":882}],[{"start":{"row":52,"column":14},"end":{"row":52,"column":15},"action":"insert","lines":["o"],"id":883}],[{"start":{"row":52,"column":15},"end":{"row":52,"column":16},"action":"insert","lines":["r"],"id":884}],[{"start":{"row":52,"column":16},"end":{"row":52,"column":17},"action":"insert","lines":["w"],"id":885}],[{"start":{"row":52,"column":17},"end":{"row":52,"column":18},"action":"insert","lines":["a"],"id":886}],[{"start":{"row":52,"column":18},"end":{"row":52,"column":19},"action":"insert","lines":["r"],"id":887}],[{"start":{"row":52,"column":19},"end":{"row":52,"column":20},"action":"insert","lines":["d"],"id":888}],[{"start":{"row":51,"column":36},"end":{"row":51,"column":51},"action":"remove","lines":["turn 90 degrees"],"id":889},{"start":{"row":51,"column":36},"end":{"row":51,"column":37},"action":"insert","lines":["m"]}],[{"start":{"row":51,"column":37},"end":{"row":51,"column":38},"action":"insert","lines":["o"],"id":890}],[{"start":{"row":51,"column":38},"end":{"row":51,"column":39},"action":"insert","lines":["v"],"id":891}],[{"start":{"row":51,"column":39},"end":{"row":51,"column":40},"action":"insert","lines":["e"],"id":892}],[{"start":{"row":51,"column":40},"end":{"row":51,"column":41},"action":"insert","lines":[" "],"id":893}],[{"start":{"row":51,"column":41},"end":{"row":51,"column":42},"action":"insert","lines":["f"],"id":894}],[{"start":{"row":51,"column":42},"end":{"row":51,"column":43},"action":"insert","lines":["o"],"id":895}],[{"start":{"row":51,"column":43},"end":{"row":51,"column":44},"action":"insert","lines":["r"],"id":896}],[{"start":{"row":51,"column":44},"end":{"row":51,"column":45},"action":"insert","lines":["w"],"id":897}],[{"start":{"row":51,"column":45},"end":{"row":51,"column":46},"action":"insert","lines":["a"],"id":898}],[{"start":{"row":51,"column":46},"end":{"row":51,"column":47},"action":"insert","lines":["r"],"id":899}],[{"start":{"row":51,"column":47},"end":{"row":51,"column":48},"action":"insert","lines":["d"],"id":900}],[{"start":{"row":53,"column":23},"end":{"row":53,"column":30},"action":"remove","lines":["Turning"],"id":901},{"start":{"row":53,"column":23},"end":{"row":53,"column":24},"action":"insert","lines":["M"]}],[{"start":{"row":53,"column":24},"end":{"row":53,"column":25},"action":"insert","lines":["o"],"id":902}],[{"start":{"row":53,"column":25},"end":{"row":53,"column":26},"action":"insert","lines":["v"],"id":903}],[{"start":{"row":53,"column":26},"end":{"row":53,"column":27},"action":"insert","lines":["i"],"id":904}],[{"start":{"row":53,"column":27},"end":{"row":53,"column":28},"action":"insert","lines":["n"],"id":905}],[{"start":{"row":53,"column":28},"end":{"row":53,"column":29},"action":"insert","lines":["g"],"id":906}],[{"start":{"row":53,"column":29},"end":{"row":53,"column":30},"action":"insert","lines":[" "],"id":907}],[{"start":{"row":53,"column":30},"end":{"row":53,"column":31},"action":"insert","lines":["F"],"id":908}],[{"start":{"row":53,"column":31},"end":{"row":53,"column":32},"action":"insert","lines":["o"],"id":909}],[{"start":{"row":53,"column":32},"end":{"row":53,"column":33},"action":"insert","lines":["r"],"id":910}],[{"start":{"row":53,"column":33},"end":{"row":53,"column":34},"action":"insert","lines":["w"],"id":911}],[{"start":{"row":53,"column":34},"end":{"row":53,"column":35},"action":"insert","lines":["a"],"id":912}],[{"start":{"row":53,"column":35},"end":{"row":53,"column":36},"action":"insert","lines":["r"],"id":913}],[{"start":{"row":53,"column":36},"end":{"row":53,"column":37},"action":"insert","lines":["d"],"id":914}],[{"start":{"row":54,"column":34},"end":{"row":54,"column":35},"action":"remove","lines":["0"],"id":915}],[{"start":{"row":54,"column":34},"end":{"row":54,"column":35},"action":"insert","lines":["1"],"id":916}],[{"start":{"row":55,"column":35},"end":{"row":55,"column":36},"action":"remove","lines":["1"],"id":917}],[{"start":{"row":55,"column":35},"end":{"row":55,"column":36},"action":"insert","lines":["0"],"id":918}],[{"start":{"row":56,"column":52},"end":{"row":57,"column":0},"action":"insert","lines":["",""],"id":919},{"start":{"row":57,"column":0},"end":{"row":57,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":57,"column":4},"end":{"row":57,"column":8},"action":"remove","lines":["    "],"id":920}],[{"start":{"row":57,"column":4},"end":{"row":58,"column":0},"action":"insert","lines":["",""],"id":921},{"start":{"row":58,"column":0},"end":{"row":58,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":58,"column":4},"end":{"row":58,"column":5},"action":"insert","lines":["d"],"id":922}],[{"start":{"row":58,"column":5},"end":{"row":58,"column":6},"action":"insert","lines":["e"],"id":923}],[{"start":{"row":58,"column":6},"end":{"row":58,"column":7},"action":"insert","lines":["f"],"id":924}],[{"start":{"row":58,"column":7},"end":{"row":58,"column":8},"action":"insert","lines":[" "],"id":925}],[{"start":{"row":58,"column":8},"end":{"row":58,"column":9},"action":"insert","lines":["g"],"id":926}],[{"start":{"row":58,"column":9},"end":{"row":58,"column":10},"action":"insert","lines":["o"],"id":927}],[{"start":{"row":58,"column":10},"end":{"row":58,"column":11},"action":"insert","lines":["a"],"id":928}],[{"start":{"row":58,"column":11},"end":{"row":58,"column":12},"action":"insert","lines":["l"],"id":929}],[{"start":{"row":58,"column":8},"end":{"row":58,"column":12},"action":"remove","lines":["goal"],"id":930},{"start":{"row":58,"column":8},"end":{"row":58,"column":21},"action":"insert","lines":["goal_callback"]}],[{"start":{"row":58,"column":21},"end":{"row":58,"column":23},"action":"insert","lines":["()"],"id":931}],[{"start":{"row":58,"column":22},"end":{"row":58,"column":23},"action":"insert","lines":["s"],"id":932}],[{"start":{"row":58,"column":23},"end":{"row":58,"column":24},"action":"insert","lines":["e"],"id":933}],[{"start":{"row":58,"column":24},"end":{"row":58,"column":25},"action":"insert","lines":["l"],"id":934}],[{"start":{"row":58,"column":25},"end":{"row":58,"column":26},"action":"insert","lines":["f"],"id":935}],[{"start":{"row":58,"column":26},"end":{"row":58,"column":27},"action":"insert","lines":[","],"id":936}],[{"start":{"row":58,"column":27},"end":{"row":58,"column":28},"action":"insert","lines":[" "],"id":937}],[{"start":{"row":58,"column":28},"end":{"row":58,"column":29},"action":"insert","lines":["g"],"id":938}],[{"start":{"row":58,"column":29},"end":{"row":58,"column":30},"action":"insert","lines":["o"],"id":939}],[{"start":{"row":58,"column":30},"end":{"row":58,"column":31},"action":"insert","lines":["a"],"id":940}],[{"start":{"row":58,"column":31},"end":{"row":58,"column":32},"action":"insert","lines":["l"],"id":941}],[{"start":{"row":58,"column":33},"end":{"row":58,"column":34},"action":"insert","lines":[":"],"id":942}],[{"start":{"row":58,"column":34},"end":{"row":59,"column":0},"action":"insert","lines":["",""],"id":943},{"start":{"row":59,"column":0},"end":{"row":59,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":58,"column":34},"end":{"row":73,"column":28},"action":"insert","lines":["","    # this callback is called when the action server is called.","    # this is the function that computes the Fibonacci sequence","    # and returns the sequence to the node that called the action server","    ","    # helper variables","    r = rospy.Rate(1)","    success = True","    ","    # define the different publishers and messages that will be used","    self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)","    self._move_msg = Twist()","    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)","    self._takeoff_msg = Empty()","    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)","    self._land_msg = Empty()"],"id":946}],[{"start":{"row":73,"column":28},"end":{"row":132,"column":14},"action":"insert","lines":["","    ","    # make the drone takeoff","    i=0","    while not i == 3:","        self._pub_takeoff.publish(self._takeoff_msg)","        rospy.loginfo('Taking off...')","        time.sleep(1)","        i += 1","    ","    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn","    sideSeconds = goal.goal","    turnSeconds = 1.8","    ","    i = 0","    for i in xrange(0, 4):","    ","      # check that preempt (cancelation) has not been requested by the action client","      if self._as.is_preempt_requested():","        rospy.loginfo('The goal has been cancelled/preempted')","        # the following line, sets the client in preempted state (goal cancelled)","        self._as.set_preempted()","        success = False","        # we end the calculation of the Fibonacci sequence","        break","    ","      # Logic that makes the robot move forward and turn","      self.move_forward_drone()","      time.sleep(sideSeconds)","      self.turn_drone()","      time.sleep(turnSeconds)","      ","      # build and publish the feedback message","      self._feedback.feedback = i","      self._as.publish_feedback(self._feedback)","      # the sequence is computed at 1 Hz frequency","      r.sleep()","    ","    # at this point, either the goal has been achieved (success==true)","    # or the client preempted the goal (success==false)","    # If success, then we publish the final result","    # If not success, we do not publish anything in the result","    if success:","      self._result.result = (sideSeconds*4) + (turnSeconds*4)","      rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result )","      self._as.set_succeeded(self._result)","        ","      # make the drone stop and land","      self.stop_drone()","      i=0","      while not i == 3:","          self._pub_land.publish(self._land_msg)","          rospy.loginfo('Landing...')","          time.sleep(1)","          i += 1","      ","if __name__ == '__main__':","  rospy.init_node('move_square')","  MoveSquareClass()","  rospy.spin()"],"id":947}],[{"start":{"row":58,"column":4},"end":{"row":127,"column":16},"action":"remove","lines":["def goal_callback(self, goal):","    # this callback is called when the action server is called.","    # this is the function that computes the Fibonacci sequence","    # and returns the sequence to the node that called the action server","    ","    # helper variables","    r = rospy.Rate(1)","    success = True","    ","    # define the different publishers and messages that will be used","    self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)","    self._move_msg = Twist()","    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)","    self._takeoff_msg = Empty()","    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)","    self._land_msg = Empty()","    ","    # make the drone takeoff","    i=0","    while not i == 3:","        self._pub_takeoff.publish(self._takeoff_msg)","        rospy.loginfo('Taking off...')","        time.sleep(1)","        i += 1","    ","    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn","    sideSeconds = goal.goal","    turnSeconds = 1.8","    ","    i = 0","    for i in xrange(0, 4):","    ","      # check that preempt (cancelation) has not been requested by the action client","      if self._as.is_preempt_requested():","        rospy.loginfo('The goal has been cancelled/preempted')","        # the following line, sets the client in preempted state (goal cancelled)","        self._as.set_preempted()","        success = False","        # we end the calculation of the Fibonacci sequence","        break","    ","      # Logic that makes the robot move forward and turn","      self.move_forward_drone()","      time.sleep(sideSeconds)","      self.turn_drone()","      time.sleep(turnSeconds)","      ","      # build and publish the feedback message","      self._feedback.feedback = i","      self._as.publish_feedback(self._feedback)","      # the sequence is computed at 1 Hz frequency","      r.sleep()","    ","    # at this point, either the goal has been achieved (success==true)","    # or the client preempted the goal (success==false)","    # If success, then we publish the final result","    # If not success, we do not publish anything in the result","    if success:","      self._result.result = (sideSeconds*4) + (turnSeconds*4)","      rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result )","      self._as.set_succeeded(self._result)","        ","      # make the drone stop and land","      self.stop_drone()","      i=0","      while not i == 3:","          self._pub_land.publish(self._land_msg)","          rospy.loginfo('Landing...')","          time.sleep(1)","          i += 1"],"id":948},{"start":{"row":58,"column":4},"end":{"row":127,"column":16},"action":"insert","lines":["def goal_callback(self, goal):","    # this callback is called when the action server is called.","    # this is the function that computes the Fibonacci sequence","    # and returns the sequence to the node that called the action server","    ","    # helper variables","    r = rospy.Rate(1)","    success = True","    ","    # define the different publishers and messages that will be used","    self._pub_cmd_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=1)","    self._move_msg = Twist()","    self._pub_takeoff = rospy.Publisher('/drone/takeoff', Empty, queue_size=1)","    self._takeoff_msg = Empty()","    self._pub_land = rospy.Publisher('/drone/land', Empty, queue_size=1)","    self._land_msg = Empty()","    ","    # make the drone takeoff","    i=0","    while not i == 3:","        self._pub_takeoff.publish(self._takeoff_msg)","        rospy.loginfo('Taking off...')","        time.sleep(1)","        i += 1","    ","    # define the seconds to move in each side of the square (which is taken from the goal) and the seconds to turn","    sideSeconds = goal.goal","    turnSeconds = 1.8","    ","    i = 0","    for i in xrange(0, 4):","    ","      # check that preempt (cancelation) has not been requested by the action client","      if self._as.is_preempt_requested():","        rospy.loginfo('The goal has been cancelled/preempted')","        # the following line, sets the client in preempted state (goal cancelled)","        self._as.set_preempted()","        success = False","        # we end the calculation of the Fibonacci sequence","        break","    ","      # Logic that makes the robot move forward and turn","      self.move_forward_drone()","      time.sleep(sideSeconds)","      self.turn_drone()","      time.sleep(turnSeconds)","      ","      # build and publish the feedback message","      self._feedback.feedback = i","      self._as.publish_feedback(self._feedback)","      # the sequence is computed at 1 Hz frequency","      r.sleep()","    ","    # at this point, either the goal has been achieved (success==true)","    # or the client preempted the goal (success==false)","    # If success, then we publish the final result","    # If not success, we do not publish anything in the result","    if success:","      self._result.result = (sideSeconds*4) + (turnSeconds*4)","      rospy.loginfo('The total seconds it took the drone to perform the square was %i' % self._result.result )","      self._as.set_succeeded(self._result)","        ","      # make the drone stop and land","      self.stop_drone()","      i=0","      while not i == 3:","          self._pub_land.publish(self._land_msg)","          rospy.loginfo('Landing...')","          time.sleep(1)","          i += 1"]}],[{"start":{"row":59,"column":0},"end":{"row":59,"column":4},"action":"insert","lines":["    "],"id":949},{"start":{"row":60,"column":0},"end":{"row":60,"column":4},"action":"insert","lines":["    "]},{"start":{"row":61,"column":0},"end":{"row":61,"column":4},"action":"insert","lines":["    "]},{"start":{"row":62,"column":0},"end":{"row":62,"column":4},"action":"insert","lines":["    "]},{"start":{"row":63,"column":0},"end":{"row":63,"column":4},"action":"insert","lines":["    "]},{"start":{"row":64,"column":0},"end":{"row":64,"column":4},"action":"insert","lines":["    "]},{"start":{"row":65,"column":0},"end":{"row":65,"column":4},"action":"insert","lines":["    "]},{"start":{"row":66,"column":0},"end":{"row":66,"column":4},"action":"insert","lines":["    "]},{"start":{"row":67,"column":0},"end":{"row":67,"column":4},"action":"insert","lines":["    "]},{"start":{"row":68,"column":0},"end":{"row":68,"column":4},"action":"insert","lines":["    "]},{"start":{"row":69,"column":0},"end":{"row":69,"column":4},"action":"insert","lines":["    "]},{"start":{"row":70,"column":0},"end":{"row":70,"column":4},"action":"insert","lines":["    "]},{"start":{"row":71,"column":0},"end":{"row":71,"column":4},"action":"insert","lines":["    "]},{"start":{"row":72,"column":0},"end":{"row":72,"column":4},"action":"insert","lines":["    "]},{"start":{"row":73,"column":0},"end":{"row":73,"column":4},"action":"insert","lines":["    "]},{"start":{"row":74,"column":0},"end":{"row":74,"column":4},"action":"insert","lines":["    "]},{"start":{"row":75,"column":0},"end":{"row":75,"column":4},"action":"insert","lines":["    "]},{"start":{"row":76,"column":0},"end":{"row":76,"column":4},"action":"insert","lines":["    "]},{"start":{"row":77,"column":0},"end":{"row":77,"column":4},"action":"insert","lines":["    "]},{"start":{"row":78,"column":0},"end":{"row":78,"column":4},"action":"insert","lines":["    "]},{"start":{"row":79,"column":0},"end":{"row":79,"column":4},"action":"insert","lines":["    "]},{"start":{"row":80,"column":0},"end":{"row":80,"column":4},"action":"insert","lines":["    "]},{"start":{"row":81,"column":0},"end":{"row":81,"column":4},"action":"insert","lines":["    "]},{"start":{"row":82,"column":0},"end":{"row":82,"column":4},"action":"insert","lines":["    "]},{"start":{"row":83,"column":0},"end":{"row":83,"column":4},"action":"insert","lines":["    "]},{"start":{"row":84,"column":0},"end":{"row":84,"column":4},"action":"insert","lines":["    "]},{"start":{"row":85,"column":0},"end":{"row":85,"column":4},"action":"insert","lines":["    "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":4},"action":"insert","lines":["    "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":4},"action":"insert","lines":["    "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"insert","lines":["    "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":4},"action":"insert","lines":["    "]},{"start":{"row":90,"column":0},"end":{"row":90,"column":4},"action":"insert","lines":["    "]},{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "]},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]},{"start":{"row":94,"column":0},"end":{"row":94,"column":4},"action":"insert","lines":["    "]},{"start":{"row":95,"column":0},"end":{"row":95,"column":4},"action":"insert","lines":["    "]},{"start":{"row":96,"column":0},"end":{"row":96,"column":4},"action":"insert","lines":["    "]},{"start":{"row":97,"column":0},"end":{"row":97,"column":4},"action":"insert","lines":["    "]},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]},{"start":{"row":101,"column":0},"end":{"row":101,"column":4},"action":"insert","lines":["    "]},{"start":{"row":102,"column":0},"end":{"row":102,"column":4},"action":"insert","lines":["    "]},{"start":{"row":103,"column":0},"end":{"row":103,"column":4},"action":"insert","lines":["    "]},{"start":{"row":104,"column":0},"end":{"row":104,"column":4},"action":"insert","lines":["    "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":4},"action":"insert","lines":["    "]},{"start":{"row":106,"column":0},"end":{"row":106,"column":4},"action":"insert","lines":["    "]},{"start":{"row":107,"column":0},"end":{"row":107,"column":4},"action":"insert","lines":["    "]},{"start":{"row":108,"column":0},"end":{"row":108,"column":4},"action":"insert","lines":["    "]},{"start":{"row":109,"column":0},"end":{"row":109,"column":4},"action":"insert","lines":["    "]},{"start":{"row":110,"column":0},"end":{"row":110,"column":4},"action":"insert","lines":["    "]},{"start":{"row":111,"column":0},"end":{"row":111,"column":4},"action":"insert","lines":["    "]},{"start":{"row":112,"column":0},"end":{"row":112,"column":4},"action":"insert","lines":["    "]},{"start":{"row":113,"column":0},"end":{"row":113,"column":4},"action":"insert","lines":["    "]},{"start":{"row":114,"column":0},"end":{"row":114,"column":4},"action":"insert","lines":["    "]},{"start":{"row":115,"column":0},"end":{"row":115,"column":4},"action":"insert","lines":["    "]},{"start":{"row":116,"column":0},"end":{"row":116,"column":4},"action":"insert","lines":["    "]},{"start":{"row":117,"column":0},"end":{"row":117,"column":4},"action":"insert","lines":["    "]},{"start":{"row":118,"column":0},"end":{"row":118,"column":4},"action":"insert","lines":["    "]},{"start":{"row":119,"column":0},"end":{"row":119,"column":4},"action":"insert","lines":["    "]},{"start":{"row":120,"column":0},"end":{"row":120,"column":4},"action":"insert","lines":["    "]},{"start":{"row":121,"column":0},"end":{"row":121,"column":4},"action":"insert","lines":["    "]},{"start":{"row":122,"column":0},"end":{"row":122,"column":4},"action":"insert","lines":["    "]},{"start":{"row":123,"column":0},"end":{"row":123,"column":4},"action":"insert","lines":["    "]},{"start":{"row":124,"column":0},"end":{"row":124,"column":4},"action":"insert","lines":["    "]},{"start":{"row":125,"column":0},"end":{"row":125,"column":4},"action":"insert","lines":["    "]},{"start":{"row":126,"column":0},"end":{"row":126,"column":4},"action":"insert","lines":["    "]},{"start":{"row":127,"column":0},"end":{"row":127,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":728,"scrollleft":0,"selection":{"start":{"row":59,"column":4},"end":{"row":127,"column":20},"isBackwards":true},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":51,"state":"start","mode":"ace/mode/python"}},"timestamp":1538578527431,"hash":"ce7c0f121258d8bbfdf84932a8a514bdf1fcf278"}