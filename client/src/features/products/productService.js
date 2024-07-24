const PRODUCTS_API = '/api/products'

//Get all products
async function getAllProducts() {
    const response = await fetch(PRODUCTS_API)

    const responseData = await response.json()

    return responseData.data
}

const productService = {
    getAllProducts,
}

export default productService
