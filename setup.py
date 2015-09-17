import setuptools

setuptools.setup(
    name="turtle-quizz-game",
    version="0.1.0",
    url="https://github.com/borntyping/cookiecutter-pypackage-minimal",

    author="Randerson Mayllon dos Santos",
    author_email="rand_mayllon@live.com",

    description="o turtle quizz game e um jogo e perguntas eobjtevias onde a cada pergunta respondida corretamente, ira automaticamente avancar para a proxima pergunta ate finalizar a fase, e caso a pergunta seja respondidaa de maneira incorreta ira voltar para o comeco do jogo.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
