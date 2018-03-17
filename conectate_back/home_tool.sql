BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `home_tool` (
	`id`	integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	varchar ( 100 ) NOT NULL,
	`technicalDetails`	varchar ( 100 ) NOT NULL,
	`description`	text NOT NULL,
	`keyWords`	varchar ( 100 ) NOT NULL,
	`associatedProjects`	text NOT NULL,
	`examplesAndActivities`	text NOT NULL,
	`pedagogicStrategy`	varchar ( 100 ) NOT NULL,
	`officialDocs`	varchar ( 100 ) NOT NULL,
	`associatedTutorials`	text NOT NULL
);
INSERT INTO `home_tool` (id,name,technicalDetails,description,keyWords,associatedProjects,examplesAndActivities,pedagogicStrategy,officialDocs,associatedTutorials) VALUES
 (3,'Foros','CentOS 7, 2GB','Los foros son herramientas colaborativas que ayudan a distribuir el conocimiento entre alumnos y profesores','Foros, Grupal','Foros de sicua, foros de moodle','Foros de sicua','Distribucion de conocimientos','Ver en: ----','Ver en .... '),
 (4,'Blogs','AmazonAMI','Blog para publicacion de noticias y articulos academicos','Blog, post, opinion','blogspot com','Actividad desarrollada en la clase de ingles','Opniones del conocimiento','ver documentacion en:','ver tutoriales en:'),
 (5,'Cacoo','Saas','Servicio alojado en lanube para crear diagramas de todo tipo','UML, Mapas, procesos','Diagramado del sistema cupi2','Diseño de bases de datos x','Dibujo creativo','Documentacion en: ','Tutoriales en '),
 (6,'Draw.io','Saas','Herramienta de diagramado uml','UML','Driagrams de clases ','Actividades de la herramienta','Online','Ver documentacion en:','Ver tutoriales en :');
COMMIT;
