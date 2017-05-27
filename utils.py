
import bcolz

save_path = "/home/docker/fastai-courses/deeplearning1/nbs/persistent/coco/"
data_path = save_path+"data/"

train_images_path = save_path+"raw_images/train2014"
val_images_path = save_path+"raw_images/val2014"

batch_folder = "batches/"
images_folder = "images/"
questions_folder = "questions/"
answers_folder = "answers/"

train_folder = "train/"


def save_array(fname, arr):
    c=bcolz.carray(arr, rootdir=fname, mode='w')
    c.flush()


def load_array(fname):
    return bcolz.open(fname)[:]

