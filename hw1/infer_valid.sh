cd ./mmdetection

python tools/test.py ../config/valid_config.py ../model.pth --out ../output_valid.pkl

cd ../

python showPkl.py ./output_valid.pkl ./output_valid.json

python filter.py ./output_valid.json ./valid_r12922016.json

rm output_valid.json output_valid.pkl