bl_info = {
    "name": "RijArray",
    "category": "Physics",
    "version": (1, 0),
    "blender": (2, 92),
    "location": "Properties Menu, F3 search or something im new to this okay",
    "description": "Quickly set up an array of rigid bodies",
    "Author": "Xyzonox",
}

import bpy
from bpy.props import *
from bpy.types import (
    AddonPreferences,
    Operator,
    Panel,
)

class OBJ_OY_array(bpy.types.Operator):
    bl_idname = "object.rij_array"
    bl_label = "RijArray"
    bl_options = {'REGISTER', 'UNDO'}
    
    x : bpy.props.FloatProperty(
        name = "X Offset",
        description = "Array X Offset",
        default = 1.5,
        min = 1.0,
        max = 100.0,
    )
    
    y : bpy.props.FloatProperty(
        name = "Y Offset",
        description = "Array Y Offset",
        default = 1.5,
        min = 1.0,
        max = 100.0,
    )
    
    z : bpy.props.FloatProperty(
        name = "Z Offset",
        description = "Array Z Offset",
        default = 1.5,
        min = 1.0,
        max = 100.0,
    )
    
    amount : bpy.props.IntProperty(
        name = "Amount",
        description = "Array count",
        default = 2,
        min = 0,
        max = 100, 
    )
    
    act : bpy.props.BoolProperty(
        name = "Execute",
        default = False,
    )

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):

        SO = bpy.context.active_object

        SO.modifiers.new("Rad Mod1", 'ARRAY')
        SO.modifiers.new("Rad Mod2", 'ARRAY')
        SO.modifiers.new("Rad Mod3", 'ARRAY')

        SO.modifiers["Rad Mod1"].relative_offset_displace[0] = self.x
        SO.modifiers["Rad Mod1"].relative_offset_displace[1] = 0
        SO.modifiers["Rad Mod1"].relative_offset_displace[2] = 0 
        SO.modifiers["Rad Mod1"].count = self.amount

        SO.modifiers["Rad Mod2"].relative_offset_displace[0] = 0
        SO.modifiers["Rad Mod2"].relative_offset_displace[1] = self.y
        SO.modifiers["Rad Mod2"].relative_offset_displace[2] = 0
        SO.modifiers["Rad Mod2"].count = self.amount

        SO.modifiers["Rad Mod3"].relative_offset_displace[0] = 0
        SO.modifiers["Rad Mod3"].relative_offset_displace[1] = 0
        SO.modifiers["Rad Mod3"].relative_offset_displace[2] = self.z
        SO.modifiers["Rad Mod3"].count = self.amount

        if self.act == True:

            bpy.ops.object.modifier_apply(modifier="Rad Mod1")
            bpy.ops.object.modifier_apply(modifier="Rad Mod2")
            bpy.ops.object.modifier_apply(modifier="Rad Mod3")

            bpy.ops.collection.create(name = "RENAME!!")

            bpy.ops.mesh.separate(type='LOOSE')

            bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_VOLUME')

            bpy.ops.rigidbody.objects_add() 

        return {'FINISHED'}

def register():
    bpy.utils.register_class(OBJ_OY_array)
    
def unregister():
    bpy.utils.unregister_class(OBJ_OY_array)
    
if __name__ == "__main__":
    register()
    
    bpy.ops.object.rij_array()