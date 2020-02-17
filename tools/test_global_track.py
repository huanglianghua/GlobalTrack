import _init_paths
import neuron.data as data
from trackers import *


if __name__ == '__main__':
    cfg_file = 'configs/qg_rcnn_r50_fpn.py'
    ckp_file = 'checkpoints/qg_rcnn_r50_fpn_coco_got10k_lasot.pth'
    transforms = data.BasicPairTransforms(train=False)
    tracker = GlobalTrack(
        cfg_file, ckp_file, transforms,
        name_suffix='qg_rcnn_r50_fpn')
    evaluators = [
        data.EvaluatorOTB(version=2015),
        data.EvaluatorLaSOT(frame_stride=10),
        data.EvaluatorGOT10k(subset='test'),
        data.EvaluatorTLP()]
    for e in evaluators:
        e.run(tracker, visualize=False)
        e.report(tracker.name)
