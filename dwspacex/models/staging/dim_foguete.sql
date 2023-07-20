
select
	distinct 
    r.rocket_id                     as "ID Foguete",
	r.rocket_name                   as "Desc. Foguete",
	r.company                       as "Empresa Foguete",
	r.engines_type                  as "Desc. Tipo Motor", 
	r.engines_number                as "Qtde. Motores",
	r.stages                        as "Qtde. Estagios",
	r.boosters                      as "Qtde. Propulsores",
	r.first_flight::date            as "Data Primeiro Lanc.",
	r.height_meters                 as "Altura (Metros)",
	r.height_feet                   as "Altura (Pés)" ,
	r.diameter_meters               as "Diametro (Metros)",
	r.diameter_feet                 as "Diametro (Pés)",
	r.mass_kg                       as "Peso (Kg)" ,
	r.mass_lb                       as "Peso (Lb)",
	r.engines_propellant_1          as "Desc. Tipo 1 Combustível" ,
	r.engines_propellant_2          as "Desc. Tipo 2 Combustível" ,
	r.landing_legs_number           as "Qtde. Pernas Pouso",
	r.landing_legs_material         as "Desc. Material Pernas Pouso",
	case
		when r.active is true then 'Sim'
		else 'Não'
	end                             as "Flag Foguete Ativo"   

from {{ source('raw', 'rockets') }} r