import argparse
from datetime import datetime as dt

parser = argparse.ArgumentParser()

# Input options
parser.add_argument('--input_json_file', default='None',
    help="Input json file detailing scene generation instructions.")
parser.add_argument('--base_scene_blendfile', default='data/base_scene.blend',
    help="Base blender file on which all scenes are based; includes " +
          "ground plane, lights, and camera.")
# parser.add_argument('--properties_json', default='data/properties2.json',
#     help="JSON file defining objects, materials, sizes, and colors. " +
#          "The \"colors\" field maps from CLEVR color names to RGB values; " +
#          "The \"sizes\" field maps from CLEVR size names to scalars used to " +
#          "rescale object models; the \"materials\" and \"shapes\" fields map " +
#          "from CLEVR material and shape names to .blend files in the " +
#          "--object_material_dir and --shape_dir directories respectively.")
parser.add_argument('--shape_dir', default='data/shapes',
    help="Directory where .blend files for object models are stored")
parser.add_argument('--material_dir', default='data/materials',
    help="Directory where .blend files for materials are stored")
# parser.add_argument('--shape_color_combos_json', default=None,
#     help="Optional path to a JSON file mapping shape names to a list of " +
#          "allowed color names for that shape. This allows rendering images " +
#          "for CLEVR-CoGenT.")

# Settings for objects
# parser.add_argument('--min_objects', default=3, type=int,
#     help="The minimum number of objects to place in each scene")
# parser.add_argument('--max_objects', default=10, type=int,
#     help="The maximum number of objects to place in each scene")
# parser.add_argument('--min_dist', default=0.25, type=float,
#     help="The minimum allowed distance between object centers")
# parser.add_argument('--margin', default=0.4, type=float,
#     help="Along all cardinal directions (left, right, front, back), all " +
#          "objects will be at least this distance apart. This makes resolving " +
#          "spatial relationships slightly less ambiguous.")
parser.add_argument('--min_pixels_per_object', default=200, type=int,
    help="All objects will have at least this many visible pixels in the " +
         "final rendered images; this ensures that no objects are fully " +
         "occluded by other objects.")
# parser.add_argument('--max_retries', default=50, type=int,
#     help="The number of times to try placing an object before giving up and " +
#          "re-placing all objects in the scene.")

# Output settings
parser.add_argument('--start_idx', default=0, type=int,
    help="The index at which to start for numbering rendered images. Setting " +
         "this to non-zero values allows you to distribute rendering across " +
         "multiple machines and recombine the results later.")
parser.add_argument('--filename_prefix', default='CLEVR',
    help="This prefix will be prepended to the rendered images and JSON scenes")
parser.add_argument('--split', default='new',
    help="Name of the split for which we are rendering. This will be added to " +
         "the names of rendered images, and will also be stored in the JSON " +
         "scene structure for each image.")
parser.add_argument('--output_image_dir', default='../output/images/',
    help="The directory where output images will be stored. It will be " +
         "created if it does not exist.")
parser.add_argument('--output_scene_dir', default='../output/scenes/',
    help="The directory where output JSON scene structures will be stored. " +
         "It will be created if it does not exist.")
parser.add_argument('--output_scene_file', default='../output/CLEVR_scenes.json',
    help="Path to write a single JSON file containing all scene information")
parser.add_argument('--output_blend_dir', default='output/blendfiles',
    help="The directory where blender scene files will be stored, if the " +
         "user requested that these files be saved using the " +
         "--save_blendfiles flag; in this case it will be created if it does " +
         "not already exist.")
parser.add_argument('--save_blendfiles', type=int, default=0,
    help="Setting --save_blendfiles 1 will cause the blender scene file for " +
         "each generated image to be stored in the directory specified by " +
         "the --output_blend_dir flag. These files are not saved by default " +
         "because they take up ~5-10MB each.")
parser.add_argument('--version', default='1.0',
    help="String to store in the \"version\" field of the generated JSON file")
parser.add_argument('--license',
    default="Creative Commons Attribution (CC-BY 4.0)",
    help="String to store in the \"license\" field of the generated JSON file")
parser.add_argument('--date', default=dt.today().strftime("%m/%d/%Y"),
    help="String to store in the \"date\" field of the generated JSON file; " +
         "defaults to today's date")

# Rendering options
parser.add_argument('--use_gpu', default=0, type=int,
    help="Setting --use_gpu 1 enables GPU-accelerated rendering using CUDA. " +
         "You must have an NVIDIA GPU with the CUDA toolkit installed for " +
         "to work.")
parser.add_argument('--width', default=320, type=int,
    help="The width (in pixels) for the rendered images")
parser.add_argument('--height', default=240, type=int,
    help="The height (in pixels) for the rendered images")
# parser.add_argument('--key_light_jitter', default=1.0, type=float,
#     help="The magnitude of random jitter to add to the key light position.")
# parser.add_argument('--fill_light_jitter', default=1.0, type=float,
#     help="The magnitude of random jitter to add to the fill light position.")
# parser.add_argument('--back_light_jitter', default=1.0, type=float,
#     help="The magnitude of random jitter to add to the back light position.")
# parser.add_argument('--camera_jitter', default=0.0, type=float,
#     help="The magnitude of random jitter to add to the camera position")
parser.add_argument('--render_num_samples', default=512, type=int,
    help="The number of samples to use when rendering. Larger values will " +
         "result in nicer images but will cause rendering to take longer.")
parser.add_argument('--render_min_bounces', default=8, type=int,
    help="The minimum number of bounces to use for rendering.")
parser.add_argument('--render_max_bounces', default=8, type=int,
    help="The maximum number of bounces to use for rendering.")
parser.add_argument('--render_tile_size', default=256, type=int,
    help="The tile size to use for rendering. This should not affect the " +
         "quality of the rendered image but may affect the speed; CPU-based " +
         "rendering may achieve better performance using smaller tile sizes " +
         "while larger tile sizes may be optimal for GPU-based rendering.")
