
import bpy
import mathutils

def main(context):
    print("Hello main")

class Tire(bpy.types.Operator):
        bl_idname = "object.tire_script"
        bl_label = "Select"
    
        def __init__(self):
            self.nameOfTire = "Tire"
            self.pos = mathutils.Vector((0, 0, 0))
            self.rot = mathutils.Vector((0, 0, 0))
            
        def execute(self, context):
            bpy.ops.object.tire_script('INVOKE_DEFAULT')
            return {'FINISHED'}    
        
        def setUp(self):
            bpy.context.active_object.location = self.pos
            bpy.context.active_object.rotation_euler = self.rot
            tires = []
            for tire , index in range(8): 
                tires.insert(index,bpy.data.objects[self.nameOfTire])
                print(index)
            # to find all objects for object in bpy.data.scenes['Scene'].objects: print(object.name)
           
            bpy.context.scene.objects.active = bpy.data.objects[self.nameOfTire1]
            bpy.context.active_object.location = self.pos
            # for object in bpy.data.scenes['Scene'].objects: print(object.name)
            for tire in range(4):
                print(str(bpy.context.active_object.rotation_euler))
                
            render_animation()
       
        def update_frame(self):
            animation = bpy.ops.anim
            animation.change_frame(frame=current_frame)

        def render_animation(self):
            global current_frame

            while current_frame < 400:
                update_frame()
                update_distance()
                render_frame()
                current_frame = current_frame + 1

        def render_frame(self):
            bpy.ops.render.render()
            bpy.context.active_object.rotation_euler = self.rot
            rot.x += 1.0


def register():
    bpy.app.handlers.frame_change_post.append(Tire)
    
def unregister():
    bpy.app.handlers.frame_change_post.remove(Tire)    
   
    
if __name__ == "__main__":
    register()
    #bpy.ops.object.tire_script()