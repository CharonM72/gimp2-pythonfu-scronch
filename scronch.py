from gimpfu import *
import os
import datetime

def scronch(img, drw):
    """Duplicates the current image, flattens the layers in the duplicate, exports it as a PNG, and then deletes the duplicate."""

    # Duplicate the image
    dup_img = img.duplicate()

    # Flatten the layers in the duplicate
    pdb.gimp_image_merge_visible_layers(dup_img, CLIP_TO_IMAGE)

    # Generate unique filename with datetime
    base_filename, ext = os.path.splitext(img.filename)
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    png_filename = "{}-{}.png".format(base_filename, now)
    
    # Export as PNG
    gimp.pdb.gimp_file_save(dup_img, dup_img.active_drawable, png_filename, png_filename)

    # Delete the duplicate image
    pdb.gimp_image_delete(dup_img)

register(
    "python-fu-scronch",
    "Scronch",
    "Duplicates the current image, flattens the layers, exports as PNG, and deletes the duplicate (i.e. scronch)",
    "Charon",
    "Copyleft",
    "2024",
    "Scronch",
    "*",  # Accepts all image types
    [
        (PF_IMAGE, "image", "Input image", None),
        (PF_DRAWABLE, "drawable", "Input drawable", None),
    ],
    [],
    scronch,
    menu="<Image>/Filters/"
)

main()