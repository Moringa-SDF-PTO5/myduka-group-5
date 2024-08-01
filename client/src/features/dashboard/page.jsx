import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getProductsCount } from '../products/productSlice'
import { getStoresCount } from '../stores/storeSlice'
import CategoryIcon from '@mui/icons-material/Category'
import InventoryIcon from '@mui/icons-material/Inventory'
import CheckCircleIcon from '@mui/icons-material/CheckCircle'
import GroupsIcon from '@mui/icons-material/Groups'
import StoreIcon from '@mui/icons-material/Store'
import Card from './Card'
import { dataLine, dataBar } from '../../assets/chartData'
import { Line, Bar } from 'react-chartjs-2'
import {
    Chart as ChartJS,
    LineElement,
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement,
} from 'chart.js'
ChartJS.register(
    LineElement,
    BarElement,
    CategoryScale,
    LinearScale,
    PointElement
)
import Spinner from '../../Components/Spinner'

const Dashboardpage = () => {
    const { isLoading, productsCount } = useSelector((state) => state.products)
    const { isStoresLoading, storesCount } = useSelector(
        (state) => state.stores
    )

    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(getProductsCount())
        dispatch(getStoresCount())
    }, [dispatch])

    if (isLoading || isStoresLoading) {
        return <Spinner />
    }

    return (
        <div className='grow p-8'>
            <h2 className='text-2x1 mb-4'>Dashboard</h2>
            <div className='grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 mb-6'>
                {/* I've commented some cards out so as to be able to show the correct data on the dashboard. My teammate still needs to be able to show their data using their relevant cards. */}
                {/* <Card
                    icon={<CategoryIcon />}
                    title='Category'
                    value={'140'}
                /> */}
                <Card
                    icon={<CheckCircleIcon />}
                    title='Products'
                    count={productsCount}
                />
                {/* <Card
                    icon={<InventoryIcon />}
                    title='Orders'
                    value={'30'}
                />
                <Card
                    icon={<GroupsIcon />}
                    title='Users'
                    value={'15'}
                /> */}
                <Card
                    icon={<StoreIcon />}
                    title='Stores'
                    count={storesCount}
                />
            </div>
            <div className=' grid grid-cols-1 lg:grid-cols-2 gap-4'>
                <div className='bg-white p-4 rounded-lg shadow-md'>
                    <h3 className='text-lg font-semibold mb-4'>Sales Data</h3>
                    <Line data={dataLine} />
                </div>
                <div className='bg-white p-4 rounded-lg shadow-md'>
                    <h3 className='text-lg font-semibold mb-4'>
                        Products Data
                    </h3>
                    <Bar data={dataBar} />
                </div>
            </div>
        </div>
    )
}

export default Dashboardpage
