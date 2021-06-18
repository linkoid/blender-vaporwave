import bpy
import bmesh

class VIEW3D_PT_vaporwave_wireframe(bpy.types.Panel):
    """Creates a Panel in the 3D Viewport under the "Vaporwave" tab"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Vaporwave"
    bl_label = "Wireframe"
    
    def draw(self, context):
        self.layout.operator("uv.embed_vaporwave_wireframe")
            
class UV_OT_embed_vaporwave_wireframe(bpy.types.Operator):
    """Embed the data for vaporwave wireframe into the active UV slot"""
    bl_idname = "uv.embed_vaporwave_wireframe"
    bl_label = "Embed Vaporwave Wireframe"

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return obj and obj.type == 'MESH' and obj.mode == 'EDIT'

    def execute(self, context):
        obj = context.active_object
        me = obj.data
        bm = bmesh.from_edit_mesh(me)

        uv_layer = bm.loops.layers.uv.verify()
        
        # adjust uv coordinates
        #for edge in bm.edges:
        #    for loop in edge.link_loops:
        #        loop_uv = loop[uv_layer]
        #        loop_uv.uv.x = not edge.smooth
        #        loop_uv.uv.y = not edge.is_manifold
        
        for face in bm.faces:
            sharp = not face.loops[-1].edge.smooth
            for loop in face.loops:
                loop_uv = loop[uv_layer]
                loop_uv.uv.x = sharp
                sharp = not loop.edge.smooth
                loop_uv.uv.y = sharp
        
        bmesh.update_edit_mesh(me)
        return {'FINISHED'}
    
classes = {
    VIEW3D_PT_vaporwave_wireframe,
    UV_OT_embed_vaporwave_wireframe
}

def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    

if __name__ == "__main__":
    register()
