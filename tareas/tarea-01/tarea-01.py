class Robot:
    def __init__(self, nom_robot="robot1",
                    nom_art=["base", "eslabon1", "eslabon2", "eslabon3", "eslabon4", "eslabon5"],
                    val_art=[0.0, 1.0, 2.0, 3.0, 4.0, 5.0],
                    pose=[10.0, 20.0, 30.0, 40.0, 50.0, 60.0]):
        self.nom_robot = nom_robot
        self.nom_art = nom_art
        self.val_art = val_art
        self.pose = pose

    def set_name(self, new_name):
        self.nom_robot = new_name

    def get_name(self):
        return self.nom_robot

    def get_articulacion(self, art_name):
        return self.val_art[self.nom_art.index(art_name)]

    def get_pose(self):
        return self.pose

def main():
    robot = Robot()
    robot.set_name("robotcito")
    print(robot.get_name())
    print(robot.get_articulacion("eslabon2"))
    print(robot.get_pose())


if __name__ == '__main__':
        main()
