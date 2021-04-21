import bpy

name_list = [
    ['Thigh.L', 'Thigh.L.IK'],
    ['Thigh.R', 'Thigh.R.IK'],
    ['Calf.L', 'Calf.L.IK'],
    ['Calf.R', 'Calf.R.IK'],
    ['Foot.L', 'Foot.L.IK'],
    ['Foot.R', 'Foot.R.IK'],
    ['Toe.L', 'Toe.L.001'],
    ['Toe.R', 'Toe.R.001'],
    ['ForeArm.L', 'ForeArm.L.IK'],
    ['ForeArm.R', 'ForeArm.R.IK'],
    ['UpperArm.L', 'UpperArm.L.IK'],
    ['UpperArm.R', 'UpperArm.R.IK'],
    ['Hand.L', 'Hand.L.IK'],
    ['Hand.R', 'Hand.R.IK']
]
objList = [obj for obj in bpy.context.selected_objects]
bpy.ops.object.select_all(action= 'DESELECT')
for obj in objList:
    v_groups = bpy.context.active_object.vertex_groups
    for n in name_list:
        if n[0] in v_groups:
            v_groups[n[0]].name = n[1]

        
#Select all meshes that you want to rename vertex groups for
#Code cobbled together by Bowl#2799 
