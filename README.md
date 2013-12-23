# OpenShift OpenERP quickstart

Este quickstart contém uma instalação do OpenERP pronta para rodar no OpenShift. Ele usa nginx para servir arquivos estáticos e roda sobre python-2.7

Se você ainda não tem uma conta na Getup, vá em http://getupcloud.com e registre-se gratuitamente.

## Crie seu app

Primeiro, crie uma aplicação com PostgreSQL:

```
$ rhc app create openerp https://reflector-getupcloud.getup.io/reflect?github=caruccio/openshift-nginx-python postgresql-9
```

Depois, faça o merge e o push deste repo para sua aplicação. Por favor seja paciente, esta operação pode demorar. 

```
$ cd openerp/
$ git remote add upstream https://github.com/caruccio/openshift-openerp-quickstart.git
$ git pull -s recursive -X theirs upstream master
$ git push
```

Pronto!

Aponte seu browser para [https://openerp-$namesapce.getup.io](https://openerp-$namesapce.getup.io) e faça login.
As credentials padrão são:

```
Username: admin
Password: admin
```

## Atualização

Este quickstart é distribuido com um build noturno do openerp, a partir do arquivo  http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-20131221-002451.tar.gz

Para atualizar o código do openerp, substitua o conteúdo do diretório `wsgi/openerp` com uma nova versão. Note que qualquer customização de código poderá ser perdida.

```
$ cd openerp/
$ wget http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-latest.tar.gz
$ tar xvf openerp-7.0-latest.tar.gz
$ mv openerp-7.0-$TIMESTAMP/* wsgi/openerp/
$ git add wsgi/openerp
$ git commit -a -m "Upgrade to version XXX"
$ git push
```
