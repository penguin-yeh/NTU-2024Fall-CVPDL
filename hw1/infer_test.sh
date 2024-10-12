cd ./mmdetection

python tools/test.py ../config/test_config.py ../model.pth --out ../output_test.pkl

cd ../

python showPkl.py ./output_test.pkl ./output_test.json

python filter.py ./output_test.json ./test_r12922016.json

rm output_test.json output_test.pkl