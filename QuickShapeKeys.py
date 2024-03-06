bl_info = {
    "name": "Shape Key Value Adjust",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class ShapeKeyValueAdjustPanel(bpy.types.Panel):
    bl_label = "Shape Key Value Adjust"
    bl_idname = "PT_ShapeKeyValueAdjustPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'

    def draw(self, context):
        layout = self.layout
        obj = context.active_object

        if obj and obj.type == 'MESH' and obj.data.shape_keys:
            shape_keys = obj.data.shape_keys.key_blocks

            for shape_key in shape_keys:
                row = layout.row()
                row.label(text=shape_key.name)
                row.prop(shape_key, "value", text="")

def register():
    bpy.utils.register_class(ShapeKeyValueAdjustPanel)

def unregister():
    bpy.utils.unregister_class(ShapeKeyValueAdjustPanel)

if __name__ == "__main__":
    register()
