select
	distinct 
    l.mission_id as "ID Missao",
	l.mission_name as "Desc. Missao",
	l.details as "Desc. Detalhes Missao"
from
	{{ source('raw', 'launches') }}   l