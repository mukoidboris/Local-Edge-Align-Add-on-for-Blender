bl_info = {
    "name": "Local Edge Align Tools",
    "author": "Boris Mukoid",
    "version": (1, 0),
    "blender": (3, 6, 0),
    "location": "View3D > Sidebar (N) > Tools Tab",
    "description": "Aligns the two vertices of each selected edge to their local center along the chosen axis.",
    "warning": "",
    "doc_url": "",
    "category": "Mesh",
}

import bpy
import bmesh
from mathutils import Vector

# ----------------------------------------------------------------------
# 1. OPERATOR (The core alignment function)
# ----------------------------------------------------------------------

BL_IDNAME = "mesh.align_edges_locally"

class AlignEdgesLocallyOperator(bpy.types.Operator):
    """Align the two vertices of each selected edge to their local center along the chosen axis."""
    bl_idname = BL_IDNAME
    bl_label = "Align Edges Locally"
    bl_options = {'REGISTER', 'UNDO'}

    axis: bpy.props.EnumProperty(
        name="Axis",
        items=[
            ('X', "X-Axis", "Align along the X-axis"),
            ('Y', "Y-Axis", "Align along the Y-axis"),
            ('Z', "Z-Axis", "Align along the Z-axis")
        ],
        description="The axis along which to align the vertices."
    )
    
    @classmethod
    def poll(cls, context):
        # The operator is only active if we are in Mesh Edit Mode
        return context.mode == 'EDIT_MESH'

    def execute(self, context):
        # Get the mesh data in edit mode
        obj = context.edit_object
        mesh = obj.data
        bm = bmesh.from_edit_mesh(mesh)

        # Map the selected axis string to its coordinate index (X=0, Y=1, Z=2)
        axis_index = {'X': 0, 'Y': 1, 'Z': 2}[self.axis]

        aligned_count = 0
        
        # Iterate over all selected edges
        for edge in bm.edges:
            if edge.select:
                # Get the coordinates of the two vertices
                v1_co = edge.verts[0].co
                v2_co = edge.verts[1].co
                
                # Calculate the center coordinate along the chosen axis for the edge
                center_co_axis = (v1_co[axis_index] + v2_co[axis_index]) / 2.0
                
                # Apply the alignment (Scale to zero locally)
                edge.verts[0].co[axis_index] = center_co_axis
                edge.verts[1].co[axis_index] = center_co_axis
                
                aligned_count += 1

        # Update the BMesh structure back to the mesh object
        bmesh.update_edit_mesh(mesh)
        self.report({'INFO'}, f"Aligned {aligned_count} edges along the {self.axis}-Axis locally.")
        return {'FINISHED'}

# ----------------------------------------------------------------------
# 2. PANEL (The persistent menu in the viewport sidebar)
# ----------------------------------------------------------------------

class VIEW3D_PT_LocalEdgeAlign(bpy.types.Panel):
    bl_label = "Local Edge Align Tools"
    bl_idname = "VIEW3D_PT_LOCAL_ALIGN"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI' # Places the panel on the sidebar (N-Panel)
    bl_category = "Tools" # The tab name where the panel will reside

    @classmethod
    def poll(cls, context):
        # Panel is only visible if a Mesh object is active and in Edit Mode
        return context.object is not None and context.object.type == 'MESH' and context.mode == 'EDIT_MESH'

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        
        # Create buttons, each calling the operator with different 'axis' parameters
        op_x = row.operator(BL_IDNAME, text="Align X", icon='AXIS_SIDE')
        op_x.axis = 'X'
        
        op_y = row.operator(BL_IDNAME, text="Align Y", icon='AXIS_FRONT')
        op_y.axis = 'Y'
        
        op_z = row.operator(BL_IDNAME, text="Align Z", icon='AXIS_TOP')
        op_z.axis = 'Z'

# ----------------------------------------------------------------------
# 3. REGISTRATION
# ----------------------------------------------------------------------

classes = (
    AlignEdgesLocallyOperator,
    VIEW3D_PT_LocalEdgeAlign
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()