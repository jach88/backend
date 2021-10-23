interface IQuery {
    page: number;
    perPage: number;
}

export const paginationSerializer = (total: number, query: IQuery):
{
    perPage: number;
    total:number;
    page:number,
    prevPage:number |null;
    nextPage:number |null;
    totalPages:number,
} => {
    const { page, perPage } = query;
    // Si el total es mayor o igual que los items por pagina entonces los items seran el perPage, coso contrario sera el total
    const itemsPerPage = total >= perPage ? perPage : total;
    // dividir
    const totalPages = Math.ceil(total / itemsPerPage);


    const prevPage = page > 1 && page <= totalPages ? page - 1 : null;

    const nextPage = totalPages > 1 && page < totalPages ? page + 1 :null;

    return{
        perPage: itemsPerPage,
        total,
        page,
        prevPage,
        nextPage,
        totalPages,
    }
}

export const paginationHelper = ({
    page,
    perPage,
}: IQuery):{skip:number; limit:number}|void =>{
   if (page && perPage){
        return{
            skip: (page -1)* perPage,
            limit: perPage,
        };
    }
};