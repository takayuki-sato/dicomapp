Empiece a trabajar con ${app}
-----------------------------------
Bienvenido a su nueva app Python.

Descripción de Python

1. [Instale la herramienta de línea de mandatos cf](${doc-url}/#starters/BuildingWeb.html#install_cf).
2. [Descargue el paquete de aplicación de inicio](${ace-url}/rest/apps/${app-guid}/starter-download).
3. Extraiga el paquete y ejecute `cd` para ir al mismo. 
4. Conéctese a Bluemix:

		cf api ${api-url}

5. Inicie la sesión en Bluemix:

		cf login -u ${username}
		cf target -o ${org} -s ${space}

6. Despliegue su app:

		cf push ${app}

7. Acceda a la app: [${ruta}](//${route})

