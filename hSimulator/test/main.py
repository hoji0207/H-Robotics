import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
print("physics on")
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.8)
# p.setTimeStep(1/200)
planeID = p.loadURDF("plane.urdf")
cubeStartPos = [2, -1, 1]
cubeStartOrientation = p.getQuaternionFromEuler([0, 0, 3.14])
robotID = p.loadURDF("r2d2.urdf", cubeStartPos, cubeStartOrientation)

p.setRealTimeSimulation(1)
for i in range(100):
    # p.stepSimulation()
    time.sleep(1)

# p.disconnect(physicsClient)