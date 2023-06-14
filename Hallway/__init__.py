bl_info = {
    "name": "Hallway",
    "author": "Hallway, Inc; Joce; BeyondDev",
    "version": (1, 0),
    "blender": (3, 5, 1),
    "location": "View3D > Snap Menu",
    "description": "Snap Objects to Active",
    "category": "Object",
}

import bpy

class OBJECT_OT_snap_objects_to_active(bpy.types.Operator):
    bl_idname = "object.snap_objects_to_active"
    bl_label = "Snap Objects to Active"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        active_obj = context.active_object
        target_location = active_obj.location

        for obj in context.selected_objects:
            if obj != active_obj:
                obj.location = target_location

        return {'FINISHED'}

def draw_func(self, context):
    layout = self.layout
    layout.operator(OBJECT_OT_snap_objects_to_active.bl_idname)

def register():
    bpy.utils.register_class(OBJECT_OT_snap_objects_to_active)
    bpy.types.VIEW3D_MT_snap.prepend(draw_func)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_snap_objects_to_active)
    bpy.types.VIEW3D_MT_snap.remove(draw_func)

if __name__ == "__main__":
    register()
