env:
    mamba env create -f environment.yml -p ~/envs/ligo
    conda activate ligo
    python -m ipykernel install --user --name mytestenv --display-name "IPython - ligo"

html:
    jupyter-book build . 
    

html-hub:
    jupyter-book config sphinx .
    sphinx-build  . _build/html -D html_baseurl=${JUPYTERHUB_SERVICE_PREFIX}/proxy/absolute/8000
    cd _build/html; python -m http.server
    

clean:
    rm -rf figurs/*; rm -rf audio/*; rm -rf _build/*