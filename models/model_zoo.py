"""Model store which handles pretrained models """
from .fcn import *
from .pspnet import *

__all__ = ['get_model', 'get_model_list', 'get_segmentation_model']

_models = {
    'fcn32s_vgg16_voc': get_fcn32s_vgg16_voc,
    'fcn16s_vgg16_voc': get_fcn16s_vgg16_voc,
    'fcn8s_vgg16_voc': get_fcn8s_vgg16_voc,
    'psp_resnet50_voc': get_psp_resnet50_voc,
    'psp_resnet50_ade': get_psp_resnet50_ade,
    'psp_resnet101_voc': get_psp_resnet101_voc,
    'psp_resnet101_ade': get_psp_resnet101_ade,
    'psp_resnet101_citys': get_psp_resnet101_citys,
    'psp_resnet101_coco': get_psp_resnet101_coco,
}


def get_model(name, **kwargs):
    name = name.lower()
    if name not in _models:
        err_str = '"%s" is not among the following model list:\n\t' % (name)
        err_str += '%s' % ('\n\t'.join(sorted(_models.keys())))
        raise ValueError(err_str)
    net = _models[name](**kwargs)
    return net


def get_model_list():
    return _models.keys()


def get_segmentation_model(model, **kwargs):
    models = {
        'fcn32s': get_fcn32s,
        'fcn16s': get_fcn16s,
        'fcn8s': get_fcn8s,
        'psp': get_psp,
    }
    return models[model](**kwargs)
