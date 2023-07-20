
select 
	lp.flight_number                                     as "Cod. Lancamento",
	lp.mission_id                                        as "ID Missao",
	lp.rocket_rocket_id                                  as "ID Foguete",
	lp.launch_site_site_id                               as "ID Plataforma",
	split_part(lp.launch_date_local,'T',1)::date         as "Data Lancamento",
	
	case 
		when lp.launch_success is true then 'Sim' 
	    else 'Não'
	end                                                  as "Flag Sucesso Lancamento",
	
	lp.launch_failure_details_reason                     as "Desc. Falha Lan.",

	case
		when lp.rocket_fairings_reused is true then 'Sim' 
		else 'Não'       
	end                                                  as "Flag Reuso Coifa",
	
	case 
		when lp.rocket_fairings_recovery_attempt is true then 'Sim'
		else 'Não'
	end                                                  as "Flag Tentat. Recuperação Coifa",
	
	case 
		when lp.rocket_fairings_recovered is true then 'Sim'
		else 'Não'
	end                                                  as "Flag Coifa Recuperada",
	lp.launch_failure_details_time                       as "Qtde. Tempo Falha Lanc.",
	lp.launch_failure_details_altitude                   as "Valor Altitude Falha Lanc.",
	rp.cost_per_launch                                   as "Valor Lancamento",
	rp.success_rate_pct                                  as "Valor Perc. Sucesso Lanc."
	
	
  from {{ source('raw', 'launches') }}   lp
  left join {{ source('raw', 'rockets') }}   rp on lp.rocket_rocket_id  = rp.rocket_id 
 where lp.launch_year in (select distinct launch_year
                            from {{ source('raw', 'launches') }}  l
                            order by launch_year desc
                            limit 5) 