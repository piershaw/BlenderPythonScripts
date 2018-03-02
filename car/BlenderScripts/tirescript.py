
import bpy
import math
from mathutils import Euler, Vector

print("Hello main")
global current_frame
global frame
sce = bpy.data.scenes[0]
pos = Vector()
nameOfTire = "Tire"
rot = Euler((0, 0, 0))
mag = Vector((0,0,0))
vo = Vector((60.0,60.0,60.0))
targetName = "Target"


bpy.data.objects[nameOfTire+"1"].location = Vector((0.3,-0.3,0))
bpy.data.objects[nameOfTire+"2"].location = Vector((-0.3,0.3,0))
bpy.data.objects[nameOfTire+"3"].location = Vector((0.3,0.3,0))
bpy.data.objects[nameOfTire+"4"].location = Vector((-0.3,-0.3,0))

tires = []
frame_num = 10 # frames in animation
rot.x = 90
rot.z = 0
objTarget = bpy.data.objects[str(targetName)]
car = bpy.data.objects["car"]


def rotate(sce):
    
    speed = mag * vo
    
    for index in range(1,5): 
        name = str(nameOfTire)+str(index)
        obj = bpy.data.objects[str(name)]
        tires.insert(index,obj)
        rot.y +=1
        vo.y = rot.y * math.pi / 180
        mag.y = objTarget.location.z
        #print("speed : "+ str(speed))
        
        #car = objTarget.location.length - obj.location.length
        print("car " + str(car.location))
        #print("> " + str(car))
        
        #print("location: "+ str(objTarget.location.z))
        rotspeed = Vector.lerp(mag,vo,speed)
        fps = (obj.location.x - objTarget.location.x)
        #print("fps : "+ str(fps))
        obj.rotation_euler = Euler((rot.x * math.pi / 180, rot.y+speed * math.pi / 180, rot.z * math.pi / 180), 'XYZ')  
        #print("name: "+ name +" : "+ str(obj.rotation_euler.y))





# run needs class later  
for anime in range(0,frame_num):
    bpy.context.scene.frame_set(frame_num)
    frame_num += 1
    sce = bpy.data.scenes[0]
    rotate(sce)
    
def register():
    bpy.app.handlers.frame_change_post.append(rotate)

if __name__ == '__main__':
    register()