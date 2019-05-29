import cv2
#import dlib
import aligndlib as adl

PRED_PATH = '/home/prathamesh/undergrad/btech_proj/misc/openface/testing/shape_predictor_68_face_landmarks.dat'

def img_capt(cam_id=0, bness=250):

    cam = cv2.VideoCapture(cam_id);

    cam.set(10, bness);

    _, fr = cam.read()

    if _:
        return True, fr;
    else:
        return False, None

def rect_to_bb(rect):
    # take a bounding predicted by dlib and convert it
    # to (x, y, w, h)
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y

    return (x, y, w, h)


def face_crop(img, affine=False, outDim=96, pred_path=PRED_PATH):
    # Script to generate cropped but not aligned face bounding box - Largest only
    if type(pred_path) == 'str':
        al = adl.AlignDlib(pred_path)
    else:
        al = pred_path

    bbx = al.getLargestFaceBoundingBox(img)

    if bbx == None:
        return False, None
    else:
        (x, y, w, h) = rect_to_bb(bbx)
        if x <= 0 or y <= 0 or w <= 0 or h <= 0:
            return False, None

        if affine:
            return True, al.align(outDim, img, bb=bbx).astype('uint8')
        else:
            return True, cv2.resize(img[y:y+h, x:x+w].astype('uint8'),(96,96))

    return False, None
